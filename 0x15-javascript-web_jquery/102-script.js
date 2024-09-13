$(document).ready(function () {
    $("INPUT#btn_translate").click(function () {
        const language_code = $("INPUT#language_code").val();  // Get the language code input
        // Fetch the translation from the API using the provided language code
        $.getJSON(`https://fourtonfish.com/hellosalut/hello/?lang=${language_code}`, function (data) {
            // Display the greeting in the div with id "hello"
            $("#hello").text(data.hello);
        });
    });
});
