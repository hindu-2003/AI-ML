<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JS Example</title>
    <style>
        #displayText {
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <p id="displayText"></p>
    <label for="nameInput">Enter Name: </label>
    <input type="text" id="nameInput" oninput="updateText()">

    <script>
        function updateText() {
            var inputText = document.getElementById('nameInput').value;
            document.getElementById('displayText').innerText = inputText;
        }
    </script>
</body>
</html>
