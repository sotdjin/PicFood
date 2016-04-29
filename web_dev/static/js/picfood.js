/**
 * Created by jin on 4/20/2016.
 */
$(document).ready(function() {
    query_images();
    $("#close-pic-modal").click(function(){
        $("#modal-pic-body").children().remove();
    });
});
function query_images() {
    var counter = 0;
    var image_counter = 1;
    var pic_counter = 0;
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
                $("#imagewrapper").append('<img id = "pic' + pic_counter + '" src=/' + imageUrl + ' onclick="display_modal(this.id)"/>')
                image_counter += 1;
                pic_counter += 1;
            }
            $("#imagewrapper").append('</div>')
            counter += 1;
        }
    });
}

function display_modal(pic_id) {
    $("#modal-pic").modal('show');
    $("#modal-pic-header").children().text(pic_id);
    $("#modal-pic-body").append('<p>BLAH BLAH BLAH BLAH BLAH</p>')
}

