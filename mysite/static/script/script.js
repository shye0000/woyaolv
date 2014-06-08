/*!
 * jQuery JavaScript Library v1.5.1
 *
 * Copyright 2011, Ziyang Zhang
 *
 * Copyright 2011, ZZY
 * Date: Wed Feb 23 13:55:29 2011 -0500
 */

$(document).ready(function(){
				//slidedown Effect
				$('.slidedown').hover(function(){
					$(this).find('.search').show();
					$(this).children().animate({bottom:'-88'},{queue:false,duration:500});
				},function(){
					$(this).children().animate({bottom:'0'},{queue:false,duration:500});
					$(this).find('.search').hide();
					}
				);
				//slideleft Effect
				$('.slideleft').hover(function(){
					$(this).children().animate({left:'-150'},{queue:false,duration:160});
					$('.news').show();
				},function(){
					$(this).children().animate({left:'0'},{queue:false,duration:160});
					$('.news').hide();
					}
				);
				//slideright Effect
				$('.slideright').hover(function(){
					$(this).children().animate({left:'140'},{queue:false,duration:160});
					$('.news2').show();
				},function(){
					$(this).children().animate({left:'0'},{queue:false,duration:160});
					$('.news2').hide();
					}
				);
				
				//startMenu Effect
				/*$('#start').toggle(function(){
					$(this).addClass('click');
					$('#startMenu').slideDown(110);
					//$('.container').addClass('small');
				},function(){
					$(this).removeClass('click');
					$('#startMenu').slideUp(110);
					//$('.container').removeClass('small');
					}
				);*/
										   
		});
	
		
			$(document).ready(function(){
				//Partial Sliding (Only show some of background)
				$('.boxgrid.peek').hover(function(){
					$(".cover", this).stop().animate({top:'90px'},{queue:false,duration:160});
				}, function() {
					$(".cover", this).stop().animate({top:'0px'},{queue:false,duration:160});
				});

			});