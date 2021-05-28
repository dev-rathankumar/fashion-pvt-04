// Regional Manager Change Password Form
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
        $(location).attr('href', '/userLogin/')
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


// Business Account Change Password Form
$(document).on('submit', '#biz_changePassword', function(e) {
  e.preventDefault();
  document.getElementById("submit").innerHTML = "Please wait...";
  var current_password = $('#current_password').val();
  var password = $('#password').val();
  var confirm_password = $('#confirm_password').val();
  var csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()


  $.ajax({
    type: 'POST',
    url: '/business/changePassword/',
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
        $(location).attr('href', 'userLogin')
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



// Ordered Products
$(document).on('submit', '#ordered_products_form', function(e) {
  e.preventDefault();
  var order_number = $('#order_number').val();
  console.log(order_number);
  exit();
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

function goBack() {
  window.history.back();
}


// Approval Swtich
function approvalSwitch(rating_id) {
  var approvalSwitch = 'approvalSwitch-' + rating_id;
  var approvalSwitch = document.getElementById(approvalSwitch);
  var status = document.getElementById("status");
  // var id =

  if (approvalSwitch.checked == true){
    var event = Boolean(true);
    toggleApproval(event, rating_id);
    // status.style.display = "block";
  } else {
    var event = Boolean(false);
    toggleApproval(event, rating_id);
     // status.style.display = "none";
  }
}

function toggleApproval(event, rating_id){
  $.ajax({
    type: 'GET',
    url: '/business/review-ratings/toggleApproval/'+rating_id,
    data: {
      event:event,
    },

    success: function(data) {
      if (data == 'true') {
        var reviewstatus = 'reviewstatus-'+rating_id;
        document.getElementById(reviewstatus).innerHTML = "Approved";
      }
      else{
        var reviewstatus = 'reviewstatus-'+rating_id;
        document.getElementById(reviewstatus).innerHTML = "Pending";
      }
    },
    error: function(data) {
      alert(data)
    }
  });
}
//
// $(document).on('submit', '#ordered_products_form', function(e) {
//   e.preventDefault();
//   var order_number = $('#order_number').val();
//   console.log(order_number);
//   exit();
//   var csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()
//
//   $.ajax({
//     type: 'POST',
//     url: '/subscribe/',
//     data: {
//       email: email,
//       csrfmiddlewaretoken: csrfmiddlewaretoken,
//     },
//
//     success: function(data) {
//       // $('#site_settings').addClass('alert alert-success alert-dismissible fade show');
//       $("#subscriptionMessage").html(data);
//     },
//     error: function(data) {
//       $("#subscriptionMessage").html("Something went wrong, please try again.");
//     }
//   });
// });
