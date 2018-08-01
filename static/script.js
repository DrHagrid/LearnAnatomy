$(function () {
        $('[data-toggle="tooltip"]').tooltip()
    })

$(document).ready(function () {
    var form = $('#check-answer');
    var hint_btn = $('#hint_btn');

    function latin_next(element_group, element_type, element_id){
        if (element_id != 0) {
            document.location.href = '/latin/' + element_group + '/' + element_type + '/' + element_id;
        }
        else {
            document.location.href = '/latin/stat/' + element_group + '/' + element_type + '/';
        }
    };

    function latin_check(element_group, element_type, element_id, answer, start){
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
                    $('.info').removeClass("invisible");
                    $('.button-box').html("");
                    $('.button-box').append('<button class="btn btn-success ans-btn" id="submit_btn" type="latin" data-action="next" data-element_group="' + element_group + '" data-element_type="' + element_type + '" data-element_id="' + data.next_element_id +'">Продолжить</button>');
                }
                else {
                    $('.alert-box').append('<div class="alert alert-danger" role="alert">' + data.replica_fail + '</div>');
                    $('#hint_btn').removeAttr("disabled");
                }
            },
            error: function(){
                console.log("ERROR");
            }
        });
    };

    function histology_check(element_id, answer, start){
        var data = {};
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
                    $('.radio-box').html("");
                    $('.info').removeClass("invisible");
                    $('.button-box').html("");
                    $('.button-box').append('<button class="btn btn-success ans-btn" id="submit_btn" type="histology" data-action="next" data-element_id="' + data.next_element_id +'">Продолжить</button>');
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

    function histology_next(element_id){
        if (element_id != 0) {
            document.location.href = '/histology/' + element_id;
        }
        else {
            document.location.href = '/histology/stat/';
        }
    };

    form.on('submit', function (e) {
        e.preventDefault();

        var submit_btn = $('#submit_btn');
        var type = submit_btn.attr("type")
        var start = submit_btn.attr("start");
        submit_btn.attr('start', 'False');

        if (type == 'latin') {
            var answer = $('#answer').val();
            var element_group = submit_btn.data("element_group");
            var element_type = submit_btn.data("element_type");
            var element_id = submit_btn.data("element_id");
            var action = submit_btn.data("action");
            if (action == 'submit') {
                latin_check(element_group, element_type, element_id, answer, start);
            }
            if (action == 'next') {
                latin_next(element_group, element_type, element_id);
            }
        }
        if (type == 'histology') {
            var element_id = submit_btn.data("element_id");
            var action = submit_btn.data("action");
            var radio = $('input[name=histology]:checked');
            var answer = radio.val()
            if (action == 'submit') {
                histology_check(element_id, answer, start);
            }
            if (action == 'next') {
                histology_next(element_id);
            }
        }
    })

    hint_btn.on('click', function (e) {
        e.preventDefault();
        var name_lat = hint_btn.data("name_lat");
        $('.hint-box').html("");
        $('.hint-box').append('<div class="alert alert-warning alert-dismissible fade show" role="alert">\n' +
            '            Подсказка: <b>' + name_lat +'</b>\n' +
            '            <button type="button" class="close" data-dismiss="alert" aria-label="Close">\n' +
            '                <span aria-hidden="true">&times;</span>\n' +
            '            </button>\n' +
            '        </div>');
    })


});