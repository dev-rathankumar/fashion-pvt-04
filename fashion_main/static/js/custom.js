setTimeout(function() {
  $('#message').fadeOut('slow');
}, 10000)

$(document).ready(function() {
  $('#CustomerPassword').keyup(function() {
    $('#strengthMessage').html(checkStrength($('#CustomerPassword').val()))
  })

  function checkStrength(password) {
    var strength = 0
    if (password.length < 6) {
      $('#strengthMessage').removeClass()
      $('#strengthMessage').addClass('Short')
      return 'Too short'
    }
    if (password.length > 7) strength += 1
    // If password contains both lower and uppercase characters, increase strength value.
    if (password.match(/([a-z].*[A-Z])|([A-Z].*[a-z])/)) strength += 1
    // If it has numbers and characters, increase strength value.
    if (password.match(/([a-zA-Z])/) && password.match(/([0-9])/)) strength += 1
    // If it has one special character, increase strength value.
    if (password.match(/([!,%,&,@,#,$,^,*,?,_,~])/)) strength += 1
    // If it has two special characters, increase strength value.
    if (password.match(/(.*[!,%,&,@,#,$,^,*,?,_,~].*[!,%,&,@,#,$,^,*,?,_,~])/)) strength += 1
    // Calculated strength value, we can return messages
    // If value is less than 2
    if (strength < 2) {
      $('#strengthMessage').removeClass()
      $('#strengthMessage').addClass('Weak')
      return 'Weak'
    } else if (strength == 2) {
      $('#strengthMessage').removeClass()
      $('#strengthMessage').addClass('Good')
      return 'Good'
    } else {
      $('#strengthMessage').removeClass()
      $('#strengthMessage').addClass('Strong')
      return 'Strong'
    }
  }
});

// Show alert if the password is not strong and do not allow registration
function giveAlert() {
  var div = document.getElementById('strengthMessage');
  strength = div.className;
  if (strength == 'Short' || strength == 'Weak') {
    alert('Please enter strong password');
    return false;
  }
}


// Regisonal Manager Password
$(document).ready(function() {
  $('#password').keyup(function() {
    $('#strengthMessage').html(checkStrength($('#password').val()))
  })

  function checkStrength(password) {
    var strength = 0
    if (password.length < 6) {
      $('#strengthMessage').removeClass()
      $('#strengthMessage').addClass('Short')
      return 'Too short'
    }
    if (password.length > 7) strength += 1
    // If password contains both lower and uppercase characters, increase strength value.
    if (password.match(/([a-z].*[A-Z])|([A-Z].*[a-z])/)) strength += 1
    // If it has numbers and characters, increase strength value.
    if (password.match(/([a-zA-Z])/) && password.match(/([0-9])/)) strength += 1
    // If it has one special character, increase strength value.
    if (password.match(/([!,%,&,@,#,$,^,*,?,_,~])/)) strength += 1
    // If it has two special characters, increase strength value.
    if (password.match(/(.*[!,%,&,@,#,$,^,*,?,_,~].*[!,%,&,@,#,$,^,*,?,_,~])/)) strength += 1
    // Calculated strength value, we can return messages
    // If value is less than 2
    if (strength < 2) {
      $('#strengthMessage').removeClass()
      $('#strengthMessage').addClass('Weak')
      return 'Weak'
    } else if (strength == 2) {
      $('#strengthMessage').removeClass()
      $('#strengthMessage').addClass('Good')
      return 'Good'
    } else {
      $('#strengthMessage').removeClass()
      $('#strengthMessage').addClass('Strong')
      return 'Strong'
    }
  }
});

// Show alert if the password is not strong and do not allow registration
function giveAlert() {
  var div = document.getElementById('strengthMessage');
  strength = div.className;
  if (strength == 'Short' || strength == 'Weak') {
    alert('Please enter strong password');
    return false;
  }
}


$(document).ready(function(){
  $("#myInput").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#myTable tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)

    });
  });
});

$(document).ready(function(){
  // $("#id_country").prop("required", true);
  $("#id_country").attr("required", "required");
})
