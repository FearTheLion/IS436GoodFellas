
$(document).ready(function($) {
    //protection vs CSS, confirming authenticity of session variables during post.
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $('#initial_input_form').on('submit', function(event){
        event.preventDefault();
        var avg_salary = $('#id_avg_starting_salary').val();
        var primary_interests = $('#id_primary_interest').serializeArray();
        submit_initial_input(avg_salary, primary_interests)
    });

     $('#gre_search_form').on('submit', function(event){
        event.preventDefault();
        var primary_interests = $('#id_primary_interest').serializeArray();
        submit_gre_search(primary_interests)
    })

});



function submit_initial_input(avg_salary, primary_interests){
    $.ajax({
        url: 'submit_initial_input/',
        type: "POST",
        data : {'avg_salary': avg_salary, 'primary_interests': JSON.stringify(primary_interests)},

        success : function(data){
            data = JSON.parse(data);
            let message = data.msg;
            let output = data.out;
            $('#output-section').html(output)
        },

        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText);
            alert("currently broken sorry");
        }
    });
}

function submit_gre_search(primary_interests){
    $.ajax({
        url: 'submit_gre_form/',
        type: "POST",
        data : {'primary_interests': JSON.stringify(primary_interests)},

        success : function(data){
            data = JSON.parse(data);
            let message = data.msg;
            let output = data.out;
            $('#output-section-gre').html(output)
        },

        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText);
            alert("currently broken sorry");
        }
    });
}