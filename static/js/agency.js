/*!
 * Start Bootstrap - Agnecy Bootstrap Theme (http://startbootstrap.com)
 * Code licensed under the Apache License v2.0.
 * For details, see http://www.apache.org/licenses/LICENSE-2.0.
 */

// jQuery for page scrolling feature - requires jQuery Easing plugin
$( document ).ready(function() {
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });
    $('.model').click(function(){
      model = $(this).attr('value');
      $('#dropdown_title').html($(this).html());
      window.open("http://www.weitz.com/wp-content/uploads/2012/08/Career-Path-Diagram_Big.jpg");
      //update_display();
    });
    
    var add_network_to_box = function() {
        	 window.open("file:///Users/jing/Dropbox/insightdata/networkbuilding/careerpath/app/static/img/results/Core3_low.jpg");
        
        }
         var add_path_to_box = function() {
            window.open("http://www.markplusinc.com/wp-content/uploads/2014/01/career-path-markplus-insight.jpg");

           // $('#path').append('<img src="http://www.markplusinc.com/wp-content/uploads/2014/01/career-path-markplus-insight.jpg">');
        }
    $('#cur_position').submit(add_network_to_box);
});

// Highlight the top nav as scrolling occurs
$('body').scrollspy({
    target: '.navbar-fixed-top'
})

// Closes the Responsive Menu on Menu Item Click
$('.navbar-collapse ul li a').click(function() {
    $('.navbar-toggle:visible').click();
});

// Show introductory modal when user arrives
//$(window).load(function(){
//    $('#ModelModal').modal('show');
//});

 	