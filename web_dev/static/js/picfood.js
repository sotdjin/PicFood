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
    var image_counter = 1;
    var image;
    $("#searchbutton").click(function() {
        var pic_counter = 0;
        var counter = 0;
        $("#imagewrapper").children().remove();
        var query = $("#searchbox").val();
        if (query != "") {
        }
        var username=document.getElementById("username").value;
        var password=document.getElementById("password").value;
        var preferences=document.getElementById("pref").value;
        $.getJSON('http://127.0.0.1:5000/' + 'algorithm',{
            username: username,
            password: password,
            preferences: preferences,
            query: query
        },
            function(data) {
                image = data;
            }
        );
        while (counter != 4) {
            $("#imagewrapper").append('<div class="row row-center">')
            for (var i = 0; i < 5; i++) {
                var imageUrl = '../static/images/yelp_photos/';
                imageUrl = imageUrl + image['results'][pic_counter];
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
    $("#modal-pic-body").append('<p>Business Name: PLACEHOLDER</p><br><p>Location: PLACEHOLDER</p><br><p>Hours: PLACEHOLDER</p>')
}

