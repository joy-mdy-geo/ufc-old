$(document).ready(function () {
    $('a#convert').bind('click', function (event) {
        $.ajax({
            type: "POST",
            url: "/_convert",
            data: {
                from_text: $('textarea[name="from_text"]').val(),
                to_encoding: $('input[name="to"]:checked').val(),
                from_encoding: $("input[name='from']:checked").val()
            }
        }).done(function (data) {
            if (data.error) {
                //  show error message
            } else {
                $("#to_text").val(data.result).show();
                $("#to_text_hint").hide();
            }
        });

        event.preventDefault();
    });
});
