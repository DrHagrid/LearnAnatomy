$(document).ready(function () {
    var form = $('#check-answer');
    var hint_btn = $('#hint_btn');

    function next(element_group, element_type, element_id){
        if (element_id != 0) {
            document.location.href = '/test/' + element_group + '/' + element_type + '/' + element_id;
        }
        else {
            document.location.href = '/stat/' + element_group + '/' + element_type + '/';
        }
    };

    function check(element_group, element_type, element_id, answer, start){
        var data = {};
        data.element_group = element_group;
        data.element_type = element_type;
        data.element_id = element_id;
        data.answer = answer;
        data.start = start;
        var csrf_token = $('#check-answer [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        var url = form.attr("action");
        console.log(data);
        $.ajax({
            url:url,
            type:'POST',
            data:data,
            cache:true,
            success: function(data){
                $('.alert-box').html("");
                if (data.response == 'True'){
                    $('.alert-box').append('<div class="alert alert-success" role="alert">' + data.replica_success + '</div>');
                    $('.answer-box').html("");
                    $('.hint-box').html("");
                    $('.answer-box').append('<b>' + data.name_lat + '</b> - ' + data.info);
                    $('.button-box').html("");
                    $('.button-box').append('<button class="btn btn-success ans-btn" id="submit_btn" data-action="next" data-element_group="' + element_group + '" data-element_type="' + element_type + '" data-element_id="' + data.next_element_id +'">Продолжить</button>');
                }
                else {
                    $('.alert-box').append('<div class="alert alert-danger" role="alert">' + data.replica_fail + '</div>');
                }
            },
            error: function(){
                console.log("ERROR");
            }
        });
    };

    form.on('submit', function (e) {
        e.preventDefault();
        var answer = $('#answer').val();
        var submit_btn = $('#submit_btn');
        var start = submit_btn.attr("start");
        submit_btn.attr('start', 'False');

        var element_group = submit_btn.data("element_group");
        var element_type = submit_btn.data("element_type");
        var element_id = submit_btn.data("element_id");
        var action = submit_btn.data("action");
        if (action == 'submit'){
            check(element_group, element_type, element_id, answer, start);
        }
        if (action == 'next') {
            next(element_group, element_type, element_id);
        }
    })

    hint_btn.on('click', function (e) {
        e.preventDefault();
        var name_lat = hint_btn.data("name_lat");
        $('.hint-box').html("");
        $('.hint-box').append('<div class="alert alert-warning hint-alert" role="alert"> Подсказка: <b>' + name_lat + '</b></div>');
    })
});
