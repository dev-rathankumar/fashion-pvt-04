// Contact Form
$(document).on('submit', '#changePassword', function(e) {
  e.preventDefault();
  document.getElementById("submit").innerHTML = "Please wait...";
  var current_password = $('#current_password').val();
  var password = $('#password').val();
  var confirm_password = $('#confirm_password').val();
  var csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()


  $.ajax({
    type: 'POST',
    url: '/regional_managers/changePassword/',
    data: {
      current_password: current_password,
      password: password,
      confirm_password: confirm_password,
      csrfmiddlewaretoken: csrfmiddlewaretoken,
    },

    success: function(data) {
      if (data == 'success') {
        document.getElementById("submit").innerHTML = "Change";
        $('#result').delay(10000).fadeOut('slow');
        $(location).attr('href', '/regional_managers/login/')
      }
      else{
        $('#result').addClass('alert alert-danger');
        $("#result").html(data);
        document.getElementById("submit").innerHTML = "Change";
        $('#result').delay(5000).fadeOut('slow');
      }
    },
    error: function(data) {
      $('#result').addClass('alert alert-danger');
      $("#result").html(data);
      document.getElementById("submit").innerHTML = "Change";
      $('#result').delay(5000).fadeOut('slow');
    }
  });
  this.reset();
});
