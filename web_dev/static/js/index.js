/**
 * Created by jin on 4/20/2016.
 */

$(document).ready(function() {
    background_image();
});

function background_image() {
    var prevnumber = 0;
    var imageStart = '../static/images/';
    var first_number = 1 + Math.floor(Math.random() * 5);
    imageStart = imageStart + "pic" + first_number.toString() + ".jpg";
    $("#indexbody").append('<img id="theimg" src=/' + imageStart + ' />');
    setInterval(function() {
        var imageUrl = '../static/images/';
        var number = 1 + Math.floor(Math.random() * 5);
        imageUrl = imageUrl + "pic" + number.toString() + ".jpg";
        $("#theimg").fadeOut(1000, function() {
            $("#theimg").attr("src", imageUrl);
        }).fadeIn(500);
    }, 5000);
}