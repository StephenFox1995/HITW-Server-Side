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
      failed();
    }
  });
}

/**
Attempts to retrieve all events from the database via
AJAX call.
@param
@param successful: Callback when a successful GET request
                   has returned json containing events.
                   Please note that the json returned may
                   contain 'null' as the value for members,
                   if there are no events in the database.
                   This callback passes one argument which
                   is the data (json) returned from the server.
@param failed: An error has occurred.*/
function ajaxGET_get_all_events(successful, failed) {
  $.ajax({
    type: 'GET',
    url: '/get_all_events/',
    contentType: 'application/json',
    dataType: 'json',
    success: function(data) {
      successful(data);
    },
    failure: function() {
      failed();
    }
  });
}

function ajaxGET_result_for_event(event_id) { }

function ajaxGET_get_result_for_member(member_id) { }

/**
Attempts to update information about a member within
the database via and AJAX call.
@param member A member object with all the new info to update.
@param successful A callback upon successful update.
@param failed A callback when an error has occurred.
*/
function ajaxPUT_update_member(member, successful, failed) {
  var jsonData = {
    "firstname" :member.get_member_f_name(),
    "lastname"  :member.get_member_l_name(),
    "handicap"  :member.get_member_handicap(),
    "identifier":member.get_member_id()
  };
  var data = JSON.stringify(jsonData)

  $.ajax({
    type: "PUT",
    url: '/edit_member/' + member.get_member_id(),
    contentType: "application/json",
    data: data,
    success: function() {
      successful();
    },
    failure: function() {
      failed();
    }
  });
}

/**
Attempts to update information about an event within the database
via an AJAX cal.
@param event The event to update.
@param successful A callback upon a successful update.
@param failed A callback when an error has occurred.
*/
function ajaxPUT_update_event(event, successful, failed) {
  // Send edited event info to server.
  var jsonData = {
    "title": event.get_event_title(),
    "location": event.get_event_location(),
    "time": event.get_event_time(),
    "date": event.get_event_date(),
    "identifier": event.get_event_id() // Use the id of the old event as ids cannot be edited.
  }
  var data = JSON.stringify(jsonData);

  $.ajax({
    type: "PUT",
    url: '/edit_event/' + event.get_event_id(),
    contentType: "application/json",
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
Attempts to delete a member from the database via an AJAX call.
@param member_id The member_id of the member to delete.
@param successful A callback upon successful deletion.
@param failed A callback when an error has occurred.
*/
function ajaxDELETE_delete_member(member_id, successful, failed) {
  $(function () {
    $.ajax({
      type: "DELETE",
      url: '/edit_member/' + member_id,
      success: function() {
        successful();
      },
      failure: function() {
        failed();
      }
    });
  });
}


function ajaxDELETE_delete_event(event_id, successful, failed) {
  $.ajax({
    type: "DELETE",
    url: '/edit_event/' + event_id,
    success: function(data) {
      successful(data);
    },
    failure: function() {
      failed();
    }
  });
}
