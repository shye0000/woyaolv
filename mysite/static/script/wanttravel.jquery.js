
// When the DOM is ready...
$(function(){
	
	// Hide stuff with the JavaScript. If JS is disabled, the form will still be useable.
	// NOTE:
	// Sometimes using the .hide(); function isn't as ideal as it uses display: none; 
	// which has problems with some screen readers. Applying a CSS class to kick it off the
	// screen is usually prefered, but since we will be UNhiding these as well, this works.
	$(".name_wrap").hide();
	$("#company_name_wrap").hide();
	$("#special_accommodations_wrap").hide();
	
	// Reset form elements back to default values
	$("#submit_button").attr("disabled",true);
	$("#num_attendees").val('Please Choose');
	$("#step_2 input[type=radio]").each(function(){
		this.checked = false;
	});
	$("#rock").each(function(){
		this.checked = false;
	});
	
	// Fade out steps 2 and 3 until ready
	$("#step_2").css({ opacity: 0.3 });
	$("#step_3").css({ opacity: 0.3 });
	$("#step_4").css({ opacity: 0.3 });
	
	$.stepTwoComplete_one = "not complete";
	$.stepTwoComplete_two = "not complete"; 
		
	// When a dropdown selection is made
	$("#num_now").change(function() {

		$(".name_wrap").slideUp().find("input").removeClass("active_name_field");
		
		switch ($("#num_now option:selected").text()) {
			case '1':
				$("#attendee_1_wrap").slideDown().find("input").addClass("active_name_field");
				break;
			case '2':
				$("#attendee_1_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_2_wrap").slideDown().find("input").addClass("active_name_field");
				break;
			case '3':
				$("#attendee_1_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_2_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_3_wrap").slideDown().find("input").addClass("active_name_field");
				break;
			case '4':
				$("#attendee_1_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_2_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_3_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_4_wrap").slideDown().find("input").addClass("active_name_field");
				break;
			case '5':	
				$("#attendee_1_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_2_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_3_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_4_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_5_wrap").slideDown().find("input").addClass("active_name_field");
				break;
				case '6':	
				$("#attendee_1_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_2_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_3_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_4_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_5_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_6_wrap").slideDown().find("input").addClass("active_name_field");
				break;
				case '7':	
				$("#attendee_1_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_2_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_3_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_4_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_5_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_6_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_7_wrap").slideDown().find("input").addClass("active_name_field");
				break;
				case '8':	
				$("#attendee_1_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_2_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_3_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_4_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_5_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_6_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_7_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_8_wrap").slideDown().find("input").addClass("active_name_field");
				break;
				case '9':	
				$("#attendee_1_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_2_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_3_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_4_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_5_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_6_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_7_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_8_wrap").slideDown().find("input").addClass("active_name_field");
				$("#attendee_9_wrap").slideDown().find("input").addClass("active_name_field");
				break;
			}
	});
	
	$(".input").blur(function(){
	
		var all_complete = true;
				
		$(".active_name_field").each(function(){
			if ($(this).val() == '' ) {
				all_complete = false;
			};
		});
		
		if (all_complete) {
			$("#step_2").removeAttr('disabled');
			$("#step_1")
			.animate({
				paddingBottom: "120px"
			})
			.css({
				"background-image": "url(/images/check.png)",
				"background-position": "bottom center",
				"background-repeat": "no-repeat"
			});
			$("#step_2").css({
				opacity: 1.0
			});
			$("#step_2 legend").css({
				opacity: 1.0 // For dumb Internet Explorer
			});
		}else{
			$("#step_1")
			.animate({
				paddingBotton: "-120px"
			})
			.css({
				"background-image": "",
			});
			//$("#step_2").attr('disabled','disabled');
			//$("#step_3").attr('disabled','disabled');

		};
	});
	
	function stepTwoTest() {
		if (($.stepTwoComplete_travelpart == "complete") && ($.stepTwoComplete_startTime == "complete")&& ($.stepTwoComplete_endTime == "complete")) 
		{
			$("#step_3").removeAttr('disabled');
			$("#step_2")
			.animate({
				paddingBottom: "120px"
			})
			.css({
				"background-image": "url(/images/check.png)",
				"background-position": "bottom center",
				"background-repeat": "no-repeat"
			});
			$("#step_3").css({
				opacity: 1.0
			});
			$("#step_3 legend").css({
				opacity: 1.0 // For dumb Internet Explorer
			});
		}else{
			$("#step_2")
			.animate({
				paddingBottom: "-120px"
			})
			.css({
				"background-image": "",
			});
			//$("#step_3").attr('disabled','disabled');
		}
	};
	
	$("#step_2 select[name=travel_part]").change(function(){
		if($(this).attr("value")!="0"){
			$.stepTwoComplete_travelpart = "complete";
		}else{
			$.stepTwoComplete_travelpart = "";
		}
		stepTwoTest();
	});
	
	$("#step_2 input[name=startTime]").blur(function(){
		if($(this).val()!=""){
			$.stepTwoComplete_startTime = "complete";
		}else{
			$.stepTwoComplete_startTime = "";
		} 
		stepTwoTest();
	});
	$("#step_2 input[name=endTime]").blur(function(){
		if($(this).val()!=""){
		$.stepTwoComplete_endTime = "complete";
		}else{
			$.stepTwoComplete_endTime = "";
		}  
		stepTwoTest();
	});
	
	$("#ok").click(function(){
		if (this.checked && $("#num_attendees option:selected").text() != '请选择'
		  	&& $.stepTwoComplete_travelpart == 'complete' && $.stepTwoComplete_startTime == 'complete'&& $.stepTwoComplete_endTime == "complete") {
				$("#submit_button").attr("disabled",false);
			} else {
				$("#submit_button").attr("disabled",true);
		}
	});
	
});