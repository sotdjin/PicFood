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
                console.log(image);
                while (counter != 4) {
                    $("#imagewrapper").append('<div class="row row-center">')
                    for (var i = 0; i < 5; i++) {
                        var imageUrl = '../static/images/yelp_photos/';
                        var image_id = image['results'][pic_counter];
                        imageUrl = imageUrl + image_id;
                        $("#imagewrapper").append('<img id = ' + image_id + ' src=/' + imageUrl + ' onclick="getBusinessID(this.id)"/>')
                        image_counter += 1;
                        pic_counter += 1;
                    }
                    $("#imagewrapper").append('</div>')
                    counter += 1;
                }
            }
        );

    });
}

var business_id;
var picture_id;
var photo_list;
var business_list;
var finished_business;
var finished_photo;

function getBusinessID(pic_id) {
    picture_id = pic_id.slice(0, -4);
    finished_business = false;
    finished_photo = false;
    var business_json = "../static/json/nv_business_information.json";
    var photo_to_business = "../static/json/photo_id_to_business.json";
    $.getJSON(photo_to_business, photo_id_callback);
    $.getJSON(business_json, business_id_callback);
}
function business_id_callback(data){
    business_list = data;
    finished_business = true;
    if (finished_photo) {
        display_modal();
    }
}
function photo_id_callback(data) {
    photo_list = data;
    finished_photo = true;
    if (finished_business) {
        display_modal();
    }
}
function display_modal() {
    var business_id = photo_list[picture_id];
    var business = business_list[business_id];
    var business_name = business['name'];
    var business_address = business['full_address'];
    var business_alcohol = business['Alcohol'];
    var business_delivery = business['Delivery'];
    var business_takeout = business['Take-out'];
    var business_wifi = business['Wi-Fi'];
    var business_rating = business['stars'];
    var business_reviewcount = business['review_count'];
    var business_categories = business['categories'];
    if (business_alcohol == null) {
        business_alcohol = 'N/A';
    }
    if (business_delivery == null) {
        business_delivery = 'N/A';
    }
    if (business_takeout == null) {
        business_takeout = 'N/A';
    }
    if (business_wifi == null) {
        business_wifi = 'N/A';
    }
    $("#modal-pic").modal('show');
    $("#modal-pic-header").children().text(business_name);
    $("#modal-pic-body").append('<p><b>Address: </b>' + business_address + '</p><p><b>Hours: </b>PLACEHOLDER</p>' +
        '<p><b>Rating: </b>' + business_rating + '</p><p><b>Review Count: </b>' + business_reviewcount + '</p>' +
        '<p><b>Alcohol: </b> ' + business_alcohol + ' </p><p><b>Delivery: </b>' + business_delivery + '</p>' +
        '<p><b>Take-Out: </b> ' + business_takeout + ' </p><p><b>Wi-Fi: </b> ' + business_wifi + ' </p>' +
        '<p><b>Categories: </b> ' + business_categories + ' </p>')
}