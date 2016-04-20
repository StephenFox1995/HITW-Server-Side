/**
Attempts to add a member to the database.
@param member The member object to add.
@param successful A callback upon a successful insertion
               into the database.
@param failure A callback when an error occurs.
*/
function ajaxPOST_add_member(member, successful, failed) {
  var member_f_name = member.get_member_f_name();
  var member_l_name = member.get_member_l_name();
  var member_handicap = member.get_member_handicap();

  var jsonData = {
    'firstname': member_f_name,
    'lastname' : member_l_name,
    'handicap' : member_handicap
  }
  var data = JSON.stringify(jsonData);

  $.ajax({
    type: 'POST',
    url: '/add_member/',
    contentType: 'application/json',
    data: data,
    success: function(data) {
      successful(data);
    },
    failure: function() {
      failed();
    }
  });
}


/**
Attempts to add a event to the database.
@param event The event to add.
@param successful A callback upon a successful
                  insertion into the database.
@param failure A callback when an error occurs.
*/
function ajaxPOST_add_event(event, successful, failed) {
  var event_title = event.get_event_title();
  var event_location = event.get_event_location();
  var event_time = event.get_event_time();
  var event_date = event.get_event_date();

  var jsonData = {
    'title'     :event_title,
    'location'  :event_location,
    'time'      :event_time,
    'date'      :event_date
  };
  var data = JSON.stringify(jsonData);

  $.ajax({
    type: 'POST',
    url: '/add_event/',
    contentType: 'application/json',
    data: data,
    success: function(data) {
      successful();
    },
    failure: function() {
      failed();
    }
  });
}

/**
Attempts to retrieve all members from the database via
AJAX call.
@param successful: Callback when a successful GET request
                   has returned json containing members.
                   Please note that the json returned may
                   contain 'null' as the value for members,
                   if there are no members in the database.
                   This callback passes one argument which
                   is the data (json) returned from the server.
@param failed: An error has occurred.*/
function ajaxGET_get_all_members(successful, failed) {
  $.ajax({
    type: 'GET',
    url: '/get_all_members/',
    contentType: 'application/json',
    dataType: 'json',
    success: function(data) {
      successful(data);
    },
    failure: function() {
      failed()
    }
  });
}

function ajax_get_event(event_id) {

}

function ajax_get_result_for_event(event_id) {

}

function ajax_get_result_for_member(member_id) {

}
