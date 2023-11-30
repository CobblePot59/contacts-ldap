$(document).ready(function(){
    $("[data-bs-target='#edit-company']").click(function(){
        var _id = $(this).data("id");
        $("#edit-company-id").val(_id);
        var name = $(this).data("name");
        $("#edit-company-name").val(name);
        var address = $(this).data("address");
        $("#edit-company-address").val(address);
        var phone = $(this).data("phone");
        $("#edit-company-phone").val(phone);
        var website = $(this).data("website");
        $("#edit-company-website").val(website);
        var tags = $(this).data("tags");
        $("#edit-company-tags").val(tags);
    });

    $("[data-bs-target='#remove-company']").click(function(){
        var _id = $(this).data("id");
        $("#rm-company-id").val(_id);
    });

    $("[data-bs-target='#upload-company']").click(function(){
    var _id = $(this).data("id");
    $("#upload-company-id").val(_id);
    });

    $('#search-input').on('input', function() {
        var searchText = $(this).val().toLowerCase();

        $('.team-member').each(function() {
            var companyName = $(this).find('#company-name').text().toLowerCase();
            var tagsName = $(this).find('#tags-name').text().toLowerCase();
            if (companyName.includes(searchText) || tagsName.includes(searchText)) {
                $(this).show();
          } else {
                $(this).hide();
          }
        });
      });
});
