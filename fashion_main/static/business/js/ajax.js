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


// Approval Switch
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


// Topbar Switch
function topbarSwitch() {
  var topbarSwitch = document.getElementById('topbarSwitch');

  var status = document.getElementById("status");

  if (topbarSwitch.checked == true){
    var event = Boolean(true);
    topbarToggleEnable(event);
    document.getElementById("topbarForm").style.display = "block";
  } else {
    var event = Boolean(false);
    topbarToggleEnable(event);
    document.getElementById("topbarForm").style.display = "none";
  }
}

function topbarToggleEnable(event){
  $.ajax({
    type: 'GET',
    url: '/business/site_settings/topbarEdit/topbarToggleEnable/',
    data: {
      event:event,
    },

    success: function(data) {
      if (data == 'enabled') {
        document.getElementById('topbarStatus').innerHTML = "Enabled";
      }
      else{
        document.getElementById('topbarStatus').innerHTML = "Disabled";
      }
    },
    error: function(data) {
      alert(data)
    }
  });
}




// $(document).on('submit', '#add_more_about1', function(e) {
//   e.preventDefault();
//   var url = $('#url').val();
//   var formData = new FormData(this);
//   $.ajax({
//       type: 'POST',
//       url: url,
//       data: formData,
//       processData: false,
//       contentType: false,
//       success: function (response) {
//         alert(response.msg)
//       },

//   });
// });


// Approval Swtich
function approvalSwitch(comment_id) {
  var approvalSwitch = 'approvalSwitch-' + comment_id;
  var approvalSwitch = document.getElementById(approvalSwitch);

  if (approvalSwitch.checked == true){
    var event = Boolean(true);
    commentApproval(event, comment_id);
  } else {
    var event = Boolean(false);
    commentApproval(event, comment_id);
  }
}

function commentApproval(event, comment_id){
  $.ajax({
    type: 'GET',
    url: '/business/blogs/comments/commentApproval/'+comment_id,
    data: {
      event:event,
    },
    success: function(data) {
      if (data == 'true') {
        var commentstatus = 'commentstatus-'+comment_id;
        document.getElementById(commentstatus).innerHTML = "Approved";
      }
      else{
        var commentstatus = 'commentstatus-'+comment_id;
        document.getElementById(commentstatus).innerHTML = "Pending";
      }
    },
    error: function(data) {
      alert(data)
    }
  });
}


// Direct Deposit Switch
function ddSwitch() {
  var ddSwitch = document.getElementById('ddSwitch');
  var url = $('#ddurl').val();
  if (ddSwitch.checked == true){
    var event = Boolean(true);
    ddToggleEnable(event, url);
    document.getElementById("ddForm").style.display = "block";
  } else {
    var event = Boolean(false);
    ddToggleEnable(event, url);
    document.getElementById("ddForm").style.display = "none";
  }
}

function ddToggleEnable(event, url){
  $.ajax({
    type: 'GET',
    url: url,
    data: {
      event:event,
    },

    success: function(data) {
      if (data == 'enabled') {
        document.getElementById('ddStatus').innerHTML = "Enabled";
      }
      else{
        document.getElementById('ddStatus').innerHTML = "Disabled";
      }
    },
    error: function(data) {
      alert(data)
    }
  });
}


// PayPal Config Switch
function ppSwitch() {
  var ppSwitch = document.getElementById('ppSwitch');
  var url = $('#ppurl').val();
  if (ppSwitch.checked == true){
    var event = Boolean(true);
    ppToggleEnable(event, url);
    document.getElementById("ppForm").style.display = "block";
  } else {
    var event = Boolean(false);
    ppToggleEnable(event, url);
    document.getElementById("ppForm").style.display = "none";
  }
}

function ppToggleEnable(event, url){
  $.ajax({
    type: 'GET',
    url: url,
    data: {
      event:event,
    },

    success: function(data) {
      if (data == 'enabled') {
        
        document.getElementById('ppStatus').innerHTML = "Enabled";
      }
      else{
        document.getElementById('ppStatus').innerHTML = "Disabled";
      }
    },
    error: function(data) {
      alert(data)
    }
  });
}

// Cash On Pickup Switch
function codSwitch() {
  var codSwitch = document.getElementById('codSwitch');
  var url = $('#codurl').val();
  if (codSwitch.checked == true){
    var event = Boolean(true);
    codToggleEnable(event, url);
  } else {
    var event = Boolean(false);
    codToggleEnable(event, url);
  }
}

function codToggleEnable(event, url){
  $.ajax({
    type: 'GET',
    url: url,
    data: {
      event:event,
    },

    success: function(data) {
      if (data == 'enabled') {
        document.getElementById('codStatus').innerHTML = "Enabled";
      }
      else{
        document.getElementById('codStatus').innerHTML = "Disabled";
      }
    },
    error: function(data) {
      alert(data)
    }
  });
}

// Blog enable Switch
function blogSwitch() {
  var blogSwitch = document.getElementById('blogSwitch');
  var url = $('#blogToggleUrl').val();
  if (blogSwitch.checked == true){
    var event = Boolean(true);
    blogToggleEnable(event, url);
  } else {
    var event = Boolean(false);
    blogToggleEnable(event, url);
  }
}

function blogToggleEnable(event, url){
  $.ajax({
    type: 'GET',
    url: url,
    data: {
      event:event,
    },

    success: function(data) {
      if (data == 'enabled') {
        var element = document.getElementById("feature");
        element.classList.remove("alert-danger");
        element.classList.add("alert-success");
        document.getElementById("enabledisable").innerHTML = "enabled";
      }
      else{
        var element = document.getElementById("feature");
        element.classList.remove("alert-success");
        element.classList.add("alert-danger");
        document.getElementById("enabledisable").innerHTML = "disabled";
      }
    },
    error: function(data) {
      alert(data)
    }
  });
}

// Product enable Switch
function productSwitch() {
  var productSwitch = document.getElementById('productSwitch');
  var url = $('#productToggleUrl').val();
  if (productSwitch.checked == true){
    var event = Boolean(true);
    productToggleEnable(event, url);
  } else {
    var event = Boolean(false);
    productToggleEnable(event, url);
  }
}

function productToggleEnable(event, url){
  $.ajax({
    type: 'GET',
    url: url,
    data: {
      event:event,
    },

    success: function(data) {
      if (data == 'enabled') {
        var element = document.getElementById("feature");
        element.classList.remove("alert-danger");
        element.classList.add("alert-success");
        document.getElementById("enabledisable").innerHTML = "enabled";
      }
      else{
        var element = document.getElementById("feature");
        element.classList.remove("alert-success");
        element.classList.add("alert-danger");
        document.getElementById("enabledisable").innerHTML = "disabled";
      }
    },
    error: function(data) {
      alert(data)
    }
  });
}


// Service enable Switch
function serviceSwitch() {
  var serviceSwitch = document.getElementById('serviceSwitch');
  var url = $('#serviceToggleUrl').val();
  if (serviceSwitch.checked == true){
    var event = Boolean(true);
    serviceToggleEnable(event, url);
  } else {
    var event = Boolean(false);
    serviceToggleEnable(event, url);
  }
}

function serviceToggleEnable(event, url){
  $.ajax({
    type: 'GET',
    url: url,
    data: {
      event:event,
    },

    success: function(data) {
      if (data == 'enabled') {
        var element = document.getElementById("feature");
        element.classList.remove("alert-danger");
        element.classList.add("alert-success");
        document.getElementById("enabledisable").innerHTML = "enabled";
      }
      else{
        var element = document.getElementById("feature");
        element.classList.remove("alert-success");
        element.classList.add("alert-danger");
        document.getElementById("enabledisable").innerHTML = "disabled";
      }
    },
    error: function(data) {
      alert(data)
    }
  });
}


// Portfolio enable Switch
function portfolioSwitch() {
  var portfolioSwitch = document.getElementById('portfolioSwitch');
  var url = $('#portfolioToggleUrl').val();
  if (portfolioSwitch.checked == true){
    var event = Boolean(true);
    portfolioToggleEnable(event, url);
  } else {
    var event = Boolean(false);
    portfolioToggleEnable(event, url);
  }
}

function portfolioToggleEnable(event, url){
  $.ajax({
    type: 'GET',
    url: url,
    data: {
      event:event,
    },

    success: function(data) {
      if (data == 'enabled') {
        var element = document.getElementById("feature");
        element.classList.remove("alert-danger");
        element.classList.add("alert-success");
        document.getElementById("enabledisable").innerHTML = "enabled";
      }
      else{
        var element = document.getElementById("feature");
        element.classList.remove("alert-success");
        element.classList.add("alert-danger");
        document.getElementById("enabledisable").innerHTML = "disabled";
      }
    },
    error: function(data) {
      alert(data)
    }
  });
}


function showhideButton()
{
    if($('#id_live_preview_button').is(":checked"))   
        $(".preview-button").show();
    else
        $(".preview-button").hide();
}



// Sale popup enable Switch
function salesPopupSwitch() {
  var salesPopupSwitch = document.getElementById('salesPopupSwitch');
  var url = $('#salesPopupToggleUrl').val();
  if (salesPopupSwitch.checked == true){
    var event = Boolean(true);
    salesPopupToggleEnable(event, url);
  } else {
    var event = Boolean(false);
    salesPopupToggleEnable(event, url);
  }
}

function salesPopupToggleEnable(event, url){
  $.ajax({
    type: 'GET',
    url: url,
    data: {
      event:event,
    },

    success: function(data) {
      if (data == 'enabled') {
        var element = document.getElementById("feature");
        element.classList.remove("alert-danger");
        element.classList.add("alert-success");
        document.getElementById("enabledisable").innerHTML = "enabled";
      }
      else{
        var element = document.getElementById("feature");
        element.classList.remove("alert-success");
        element.classList.add("alert-danger");
        document.getElementById("enabledisable").innerHTML = "disabled";
      }
    },
    error: function(data) {
      alert(data)
    }
  });
}



// Approval Switch
function testimonialSwitch(testi_id) {
  var approvalSwitch = 'testimonialSwitch-' + testi_id;
  var approvalSwitch = document.getElementById(approvalSwitch);
  if (approvalSwitch.checked == true){
    var event = Boolean(true);
    testimonialApproval(event, testi_id);
    // status.style.display = "block";
  } else {
    var event = Boolean(false);
    testimonialApproval(event, testi_id);
     // status.style.display = "none";
  }
}


function testimonialApproval(event, testi_id){
  $.ajax({
    type: 'GET',
    url: '/business/testimonials/testimonialApproval/'+testi_id,
    data: {
      event:event,
    },

    success: function(data) {
      if (data == 'true') {
        var testimonialstatus = 'testimonialstatus-'+testi_id;
        document.getElementById(testimonialstatus).innerHTML = "Approved";
      }
      else{
        var testimonialstatus = 'testimonialstatus-'+testi_id;
        document.getElementById(testimonialstatus).innerHTML = "Pending";
      }
    },
    error: function(data) {
      alert(data)
    }
  });
}

// Language enable Switch
function langSwitch() {
  var langSwitch = document.getElementById('langSwitch');
  var url = $('#langToggleUrl').val();
  if (langSwitch.checked == true){
    var event = Boolean(true);
    langToggleEnable(event, url);
  } else {
    var event = Boolean(false);
    langToggleEnable(event, url);
  }
}

function langToggleEnable(event, url){
  $.ajax({
    type: 'GET',
    url: url,
    data: {
      event:event,
    },

    success: function(data) {
      if (data == 'enabled') {
        var element = document.getElementById("feature");
        element.classList.remove("alert-danger");
        element.classList.add("alert-success");
        document.getElementById("enabledisable").innerHTML = "enabled";
      }
      else{
        var element = document.getElementById("feature");
        element.classList.remove("alert-success");
        element.classList.add("alert-danger");
        document.getElementById("enabledisable").innerHTML = "disabled";
      }
    },
    error: function(data) {
      alert(data)
    }
  });
}
