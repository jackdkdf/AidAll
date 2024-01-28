$(document).ready(function () {
    console.log("TEST2")
    $("#apply-form").submit(function (event) {
        var formData = $('#apply-form').serialize();
        $.ajax({
          type: "POST",
          url: "applications/create/ajax",
          data: formData,
          dataType: "json",
          encode: true,
        }).done(function (data) {
          console.log(data);
        });
    
        event.preventDefault();
    });
  });