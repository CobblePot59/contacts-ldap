$(document).ready(function(){
    $("[data-bs-target='#edit-employee']").click(function(){
        var _id = $(this).data("id");
        $("#edit-employee-id").val(_id);
        var name = $(this).data("name");
        $("#edit-employee-name").val(name);
        var surname = $(this).data("surname");
        $("#edit-employee-surname").val(surname);
        var email = $(this).data("email");
        $("#edit-employee-email").val(email);
        var phone = $(this).data("phone");
        $("#edit-employee-phone").val(phone);
        var mphone = $(this).data("mphone");
        $("#edit-employee-mphone").val(mphone);
        var job = $(this).data("job");
        $("#edit-employee-job").val(job);
        var companyName = $(this).data("company-name");
        $("#edit-employee-company-name").val(companyName);
    });

    $("[data-bs-target='#remove-employee']").click(function(){
        var _id = $(this).data("id");
        $("#rm-employee-id").val(_id);
    });

    $("[data-bs-target='#upload-employee']").click(function(){
    var _id = $(this).data("id");
    $("#upload-employee-id").val(_id);
    });

    $('#search-input').on('input', function() {
        var filter = $(this).val().toLowerCase();

        $('.team-member').each(function() {
            var employeeName = $(this).find('#employee-name').text().toLowerCase();
            if (employeeName.includes(filter)) {
                $(this).show();
            } else {
                $(this).hide();
            }
        });
    });
});
