/**
 * Created by jin on 4/20/2016.
 */

$(document).ready(function() {
    //background_image();
});

function background_image() {
    var prevnumber = 0;
    var number = 0;
    var imageStart = '../static/images/';
    var first_number = 1 + Math.floor(Math.random() * 5);
    imageStart = imageStart + "pic" + first_number.toString() + ".jpg";
    $("#indexbody").append('<img id="theimg" src=/' + imageStart + ' />');
    setInterval(function() {
        prevnumber = number;
        var imageUrl = '../static/images/';
        number = 1 + Math.floor(Math.random() * 5);
        if (prevnumber != number) {
            imageUrl = imageUrl + "pic" + number.toString() + ".jpg";
            $("#theimg").fadeOut(1000, function() {
                $("#theimg").attr("src", imageUrl);
            }).fadeIn(500);
        }
    }, 5000);
}