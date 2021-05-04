$(document).on('submit', '#save_setting_form', function(e) {
  e.preventDefault();
  // var business = $('#id_business').val();
  var site_title = $('#id_site_title').val();
  var site_logo = $('#id_site_logo').val();
  var copyright = $('#id_copyright').val();
  var csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()

  $.ajax({
    type: 'POST',
    url: '/business/site-settings/',
    data: {
      // business : business,
      site_title: site_title,
      site_logo: site_logo,
      copyright: copyright,
      csrfmiddlewaretoken: csrfmiddlewaretoken,
    },

    success: function(data) {
      // $('#site_settings').addClass('alert alert-success alert-dismissible fade show');
      // $("#site_settings").html(data);
      alert(data);
    },
    error: function(data) {
      alert(data);
    }
  });
});


function updCart(id) {

  var csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()
  var form = $('#qtyForm' + id)
  alert(csrfmiddlewaretoken)

  $.ajax({
    url: '/cart/add_cart_ajax/' + id + '/',
    type: 'POST',
    data: {
      form: form,
      csrfmiddlewaretoken: csrfmiddlewaretoken,
    },
    success: function(data) {
      alert(data);
    },
  });
}


// Newsletters
$(document).on('submit', '#newsletterForm', function(e) {
  e.preventDefault();
  var email = $('#email').val();
  var csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()

  $.ajax({
    type: 'POST',
    url: '/subscribe/',
    data: {
      email: email,
      csrfmiddlewaretoken: csrfmiddlewaretoken,
    },

    success: function(data) {
      // $('#site_settings').addClass('alert alert-success alert-dismissible fade show');
      $("#subscriptionMessage").html(data);
    },
    error: function(data) {
      $("#subscriptionMessage").html("Something went wrong, please try again.");
    }
  });
});



// Send an inquiry
$(document).on('submit', '#inquiry-modal', function(e) {
  e.preventDefault();
  $("#submit").val('Please wait...');
  var business_id = $('#business_id').val();
  var user_id = $('#user_id').val();
  var product_id = $('#product_id').val();
  var product_name = $('#product_name').val();
  var first_name = $('#first_name').val();
  var last_name = $('#last_name').val();
  var email = $('#email').val();
  var phone = $('#phone').val();
  var inq_message = $('#inq_message').val();
  var csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()

  $.ajax({
    type: 'POST',
    url: '/inquiry/',
    data: {
      business_id: business_id,
      user_id: user_id,
      product_id: product_id,
      product_name: product_name,
      first_name: first_name,
      last_name: last_name,
      email: email,
      phone: phone,
      inq_message: inq_message,
      csrfmiddlewaretoken: csrfmiddlewaretoken,
    },

    success: function(data) {
      if (data == 'already-inquired') {
        $('#inquiry_success').addClass('alert alert-warning alert-dismissible fade show');
        $("#inquiry_success").html('You have already made an inquiry about this product. Please wait until we get back to you.');
        $("#submit").val('Send Inquiry');
      } else {
        $('#inquiry_success').addClass('alert alert-success alert-dismissible fade show');
        $("#inquiry_success").html(data);
        $("#submit").val('Sent');
        $('#inquiry_success').delay(4000).fadeOut('slow');
      }
    },
    error: function(data) {
      $('#inquiry_success').addClass('alert alert-danger alert-dismissible fade show');
      $("#inquiry_success").html("Something went wrong, please try again.");

    }
  });
  this.reset();
});


// Contact Form
$(document).on('submit', '#contact_form', function(e) {
  e.preventDefault();
  $("#submit").val('Please wait...');
  var business_id = $('#business_id').val();
  var user_id = $('#user_id').val();
  var name = $('#name').val();
  var email = $('#email').val();
  var phone = $('#phone').val();
  var subject = $('#subject').val();
  var contact_message = $('#contact_message').val();
  var csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()


  $.ajax({
    type: 'POST',
    url: '/contact/',
    data: {
      business_id: business_id,
      user_id: user_id,
      name: name,
      email: email,
      phone: phone,
      subject: subject,
      contact_message: contact_message,
      csrfmiddlewaretoken: csrfmiddlewaretoken,
    },

    success: function(data) {
      if (data == 'otp sent') {
        $('.otp_form').slideDown();
        $('#contactMessage').addClass('alert alert-success');
        $("#contactMessage").html('OTP has been sent to your email address. Please verify it.');
        $("#submit").val('Verification Required');
        $('#contactMessage').delay(4000).fadeOut('slow');
        // return count_down_otp();
      }
    },
    error: function(data) {
      $('#contactMessage').addClass('alert alert-danger');
      $("#contactMessage").html("Something went wrong, please try again.");
    }
  });
  this.reset();
});



// Contact OTP Form
$(document).on('submit', '#contact_otp_form', function(e) {
  e.preventDefault();
  $("#otpsubmit").val('Verifying...');
  var otp = $('#otp').val();
  var csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()

  $.ajax({
    type: 'POST',
    url: '/verify_otp/',
    data: {
      otp: otp,
      csrfmiddlewaretoken: csrfmiddlewaretoken,
    },

    success: function(data) {
      if (data == 'verified') {
        $('#OTPsuccess').addClass('alert alert-success');
        $("#OTPsuccess").html('OTP Verified. Your message has been submitted successfully.');
        $("#otpsubmit").val('OTP Verified');
        $("#otpsubmit").css("backgroundColor", "green");
        $("#otpsubmit").prop('disabled', true);
        $("#resendotp").css("display", "none");
        $('#OTPsuccess').delay(7000).fadeOut('slow');
      } else if (data == 'wrong-otp') {
        $('#OTPfailed').addClass('alert alert-danger');
        $("#OTPfailed").html('Invalid OTP');
        $("#otpsubmit").val('Verify');
        $('#OTPfailed').delay(5000).fadeOut('slow');
      }
      else{
        alert(data);
        $("#otpsubmit").val('Verify');
      }
    },
    error: function(data) {
      $('#OTPmessage').addClass('alert alert-danger');
      $("#OTPmessage").html("Something went wrong, please try again.");
    }
  });
  this.reset();
});


function resendOTP(){
  // $("#countdown").css("display", "none");
  document.getElementById("resendotp").innerHTML = "Please wait...";
  $.ajax({
    type: 'GET',
    url: '/resend_otp/',
    data: {
      // otp: 'resend-otp',
    },

    success: function(data) {
      if (data == 'otp sent') {
        document.getElementById("resendotp").innerHTML = "Resend OTP";
        $('#contactMessage').addClass('alert alert-success');
        alert('OTP has been sent to your email address. Please verify it.');
        $("#submit").val('Verification Required');
      }
      else{
        document.getElementById("resendotp").innerHTML = "Resend OTP";
        alert(data);
      }
    },
    error: function(data) {
      document.getElementById("resendotp").innerHTML = "Resend OTP";
      $('#OTPmessage').addClass('alert alert-danger');
      $("#OTPmessage").html("Something went wrong, please try again.");
    }
  });

}


// function count_down_otp(){
//   var timeleft = 90;
//   var downloadTimer = setInterval(function(){
//     if(timeleft <= 0){
//       clearInterval(downloadTimer);
//       document.getElementById("countdown").innerHTML = "Your OTP has been expired.";
//       $("#countdown").css("color", "red");
//     } else {
//       document.getElementById("countdown").innerHTML =  "Your OTP will be expired in <b>" + timeleft + "</b> seconds.";
//     }
//     timeleft -= 1;
//   }, 1000);
// }



$('#id_state').change(function(){
    var state_id = $(this).val();
    var url = "/fetchTax/taxByState/"
$.ajax({
    type: "GET",
    url: url,
    data: {
      state_id: state_id,
      dataType: "json",
    },
    success: function( data ) {
        console.log(data);
        document.getElementById("tax_percent").innerHTML = data.tax_percent;
        document.getElementById("tax_amount").innerHTML = data.tx_amount;
        document.getElementById("grand_total").innerHTML = data.grand_total;
    }
});
});
