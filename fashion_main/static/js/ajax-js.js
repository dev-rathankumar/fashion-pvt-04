
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


function updCart(id){

  var csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()
  var form = $('#qtyForm'+id)
  alert(csrfmiddlewaretoken)

  $.ajax({
    url: '/cart/add_cart_ajax/' + id + '/',
    type:'POST',
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