/**
Attempts to add a member to the database.
@param member The member object to add.
@param successful A callback upon a successful insertion
               into the database.
@param failure A callback when an error occurs.
*/
function ajaxPOST_add_member(member, successful, failure) {
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
      failure();
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
function ajaxPOST_add_event(event, successful, failure) {
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
      failure();
    }
  });
}
function ajax_get_member(member_id) {

}

function ajax_get_event(event_id) {

}

function ajax_get_result_for_event(event_id) {

}

function ajax_get_result_for_member(member_id) {

}
