<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Form Page</title>
  </head>
  <body>
    <h1>Welcom to the Form!</h1>
    <form action="/submit" method="POST">
      <div>
        <label for="username">Enter your name:</label>
        <input type="text" id="username" name="username" required />
      </div>
      <div>
        <button type="submit">Submit</button>
      </div>
    </form>
  </body>
</html>
