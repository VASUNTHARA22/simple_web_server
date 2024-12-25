# EX01 Developing a Simple Webserver

# Date:12.09.2024
# AIM:
To develop a simple webserver to serve html pages and display the configuration details of laptop.

# DESIGN STEPS:
## Step 1:
HTML content creation.

## Step 2:
Design of webserver workflow.

## Step 3:
Implementation using Python code.

## Step 4:
Serving the HTML pages.

## Step 5:
Testing the webserver.

# PROGRAM:
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Laptop Configuration</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        select, input {
            width: 100%;
            padding: 8px;
            margin: 5px 0;
        }
        .submit-btn {
            background-color: #166c19;
            color: white;
            padding: 10px 15px;
            border: none;
            cursor: pointer;
        }
        .submit-btn:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body style ="background-color: lightblue">
    <h1>Laptop Configuration</h1>
    <form action="/submit" method="post">
        <div class="form-group">
            <label for="processor">Processor</label>
            <select id="processor" name="processor" required>
                <option value="">-- Select Processor --</option>
                <option value="i5">Intel Core i5</option>
                <option value="i7">Intel Core i7</option>
                <option value="i9">Intel Core i9</option>
                <option value="ryzen5">AMD Ryzen 5</option>
                <option value="ryzen7">AMD Ryzen 7</option>
            </select>
        </div>
        <div class="form-group">
            <label for="ram">RAM</label>
            <select id="ram" name="ram" required>
                <option value="">-- Select RAM --</option>
                <option value="8gb">8 GB</option>
                <option value="16gb">16 GB</option>
                <option value="32gb">32 GB</option>
            </select>
        </div>
        <div class="form-group">
            <label for="storage">Storage</label>
            <select id="storage" name="storage" required>
                <option value="">-- Select Storage --</option>
                <option value="256gb-ssd">256 GB SSD</option>
                <option value="512gb-ssd">512 GB SSD</option>
                <option value="1tb-ssd">1 TB SSD</option>
            </select>
        </div>
        <div class="form-group">
            <label for="display">Display</label>
            <select id="display" name="display" required>
                <option value="">-- Select Display --</option>
                <option value="1080p">1080p Full HD</option>
                <option value="1440p">1440p Quad HD</option>
                <option value="4k">4K Ultra HD</option>
            </select>
        </div>
        <div class="form-group">
            <label for="custom-message">Additional Notes</label>
            <textarea id="custom-message" name="customMessage" rows="4" placeholder="Enter any special requirements..."></textarea>
        </div>
        <button type="submit" class="submit-btn">Submit Configuration</button>
    </form>
</body>
</html>
```

# OUTPUT:

![alt text](<simpl web server.png>)



# RESULT:
The program for implementing simple webserver is executed successfully.
