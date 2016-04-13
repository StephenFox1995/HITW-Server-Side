// Parses json for members.
function parse_member_from_json(data) {
  var members = []
  $.each(data, function(index, element) {
    $.each(element, function(i, json) {
      member_f_name =     json['firstname']
      member_l_name =     json['lastname']
      member_handicap =   json['handicap']
      member_id =         json['identifier']
      var member = new Member(member_id, member_f_name, member_l_name, member_handicap)
      members.push(member);
    });
  });
  return members;
};
