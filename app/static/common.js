/**
Attempts to add a member to the database.
@param member The member object to add.
@param success A callback upon a successful insertion
               into the database.
@param failer A callback when an error occurs.
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

function ajax_get_member(member_id) {

}

function ajax_get_event(event_id) {

}

function ajax_get_result_for_event(event_id) {

}

function ajax_get_result_for_member(member_id) {

}
