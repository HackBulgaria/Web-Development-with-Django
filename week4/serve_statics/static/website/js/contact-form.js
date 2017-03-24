$("#contactForm").validator({
	disable: false

}).on("submit", function (event) {
	if (event.isDefaultPrevented()) {
		submitMSG(false, function () {
			$("#contact-form-result").html('<a href="#" class="close" data-dismiss="alert">&times;</a> Please, fill the empty required fields.');
		});


	} else {
		// everything looks good!
		event.preventDefault();
		submitForm();
	}
});

function getBaseUrl() {
    var re = new RegExp(/^.*\//);
    return re.exec(window.location.href);
}

function submitForm() {
	// Initiate Variables With Form Content
	var name = $("#name").val();
	var email = $("#email").val();
	var subject = $("#subject").val();
	var message = $("#message").val();

	$.ajax({
		type: "POST",
		url: getBaseUrl() + "include/contactForm.php",
		data: "name=" + name + "&email=" + email + "&subject=" + subject + "&message=" + message,
		success: function (text) {
			if (text == "success") {
				formSuccess();
			} else {
				submitMSG(false, text);
			}
		}
	});
}

function formSuccess() {
	$("#contactForm")[0].reset();
	submitMSG(true, function () {

		$("#contact-form-result").html('<a href="#" class="close" data-dismiss="alert">&times;</a> We have <strong>successfully</strong> received your Message and will get Back to you as soon as possible.')

	});
}

function submitMSG(valid, msg) {
	if (valid) {
		var msgClasses = "alert alert-success";
	} else {
		var msgClasses = "alert alert-danger";
	}
	$("#contact-form-result").removeClass().addClass(msgClasses).text(msg);
}
