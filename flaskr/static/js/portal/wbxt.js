function post_wbxt_notification(message) {
    console.log("Sending Notification - " + message)

    param = jQuery.param(
        {
            'room_name': 'LAB-2754 Space',
            'text': message
        });

	return $.ajax({
		type: 'POST',
		url: '/api/v1/wbxt/send_message?' + param
	});
}