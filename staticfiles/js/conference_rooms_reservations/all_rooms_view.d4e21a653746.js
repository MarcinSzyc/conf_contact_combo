$(function () {

    let remove_button = $(".btn-outline-danger")

   remove_button.click(function (e) {
        var retVal = confirm("Are you sure ?");
        var item_id = $(this).data("id")
        console.log(e.target)
        if (retVal == true) {
            $.ajax({
                url: `http://localhost:8000/conf_rooms_reservations/room/delete/${item_id}`,
                data: {
                    // csrfmiddlewaretoken: `${$(this).data("token")}`
                },
                type: "delete",
                dataType: "json"
            }).done(function () {
                // remove_button.closest('tr').remove()
            }).always(function () {
                e.target.closest('tr').remove()
            })
        } else {
            location.reload()
        }
    })

    // using jQuery
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // var csrftoken = getCookie('csrftoken');
    var csrftoken = $(".btn-outline-danger").data("token")

    // console.log(csrftoken)

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


})

