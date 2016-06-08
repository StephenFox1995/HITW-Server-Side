/**
	Parses json representation of a member into a member object.

	@param data 	The json data.
	@return An array containing members parsed.
*/
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


/**
	Parses json representation of a event into a event object.

	@param data 	The json data.
	@return An array containing events parsed.
*/
function parse_event_from_json(data) {
  var events = []
  $.each(data, function(index, element) {
    $.each(element, function(i, json) {
      event_id =        json['identifier']
      event_title =     json['title']
      event_location =  json['location']
      event_start_tee = json['startTeeTime']
      event_end_tee =   json['endTeeTime']
      event_date =      json['date']
      var eventHITW = new EventHITW(event_id, event_title, event_location, event_start_tee, event_end_tee, event_date)
      events.push(eventHITW)
    })
  });
  return events;
}


/**
	Parses json representation of a event images into an array of base64 strings.

	@param data 	The json data.
	@return An array containing base64 strings that were parsed. parsed.
*/
function parse_event_images_from_json(data) {
  var event_images = []
  $.each(data, function(index, element) {
    $.each(element, function(i, json) {
      image_data = json['image'];
      event_images.push(image_data);
    })
  });
  return event_images;
}


/**
  Parses
*/
function parse_poys(data) {
  var poysArray = [];
  var years = parsePoysYearsArray(data);
  var currentYear;

  var poys = data.poys;

  $.each(poys, function(index, year) {
    // Get the current year.
    currentYear = years[index]

    $.each(year, function(index, poys) {
      $.each(poys, function(index, poy) {
        poy.year = currentYear;
        poysArray.push(poy)
      });
    });
  });
  return poysArray
}


function parsePoysYearsArray(data) {
  return data.years
}



/**
	Parses json representation of a result into a result object.

	@param data 	The json data.
	@return An array containing results parsed.
*/
function parse_result_from_json(data) {
  var results = []
  $.each(data, function(index, element) {
    $.each(element, function(i, json) {
      event_id =       json['event_id']
      member_id   =    json['member_id']
      score          = json['score']
      var result = new Result(event_id, member_id, score);
      results.push(result);
    })
  });
  return results;
}


function getUrlVars() {
    var vars = [], hash;
    var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
    for(var i = 0; i < hashes.length; i++) {
        hash = hashes[i].split('=');
        vars.push(hash[0]);
        vars[hash[0]] = hash[1];
    }
    return vars;
}

/**
	Strips the data:image/jpeg;base64 from the beginning of a base64 encoded string.

	@param base64string 	The base 64 encoded data.
*/
function strip_meta_data_base64(base64string) {
  return base64string.replace(/^data:image\/(png|jpeg);base64,/, "");
}



function get_object_for_button_index(button, array) {
  var index = $(button).closest('tr').index();
  return array[index];
}


function validTimeFormat(timeString) {
  // Regular expression to match required time format
   var expression = /^\d{1,2}:\d{2}([ap]m)?$/;
   return timeString.match(expression)
}


function validateInput(input) {
  if ((input === undefined ||
      input === null ||
      input === '' ||
      input === 'dd/mm/yy' ||
      input === 'dd-mm-yy')) {
    return false;
  }
  return true;
}
