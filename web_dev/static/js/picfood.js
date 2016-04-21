/**
 * Created by jin on 4/20/2016.
 */
$(document).ready(function() {
    query_images();
});
function query_images() {
    var counter = 0;
    var image_counter = 1;
    $("#searchbutton").click(function() {
        var query = $("#searchbox").val();
        if (query != "") {
            $("#imagewrapper").append('<div class="row"><div class="col-md-12"><div class="text-center"><p>' + query + '</p></div></div></div>');
        }
        while (counter != 4) {
            $("#imagewrapper").append('<div class="row row-center">')
            for (var i = 0; i < 5; i++) {
                var imageUrl = '../static/images/';
                imageUrl = imageUrl + "fp" + image_counter.toString() + ".jpg";
                $("#imagewrapper").append('<img src=/' + imageUrl + ' />')
                image_counter += 1;
            }
            $("#imagewrapper").append('</div>')
            counter += 1;
        }
    });
}