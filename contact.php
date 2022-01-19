<?php

$sendTo = "leocableiva@gmail.com";

$action = $_POST['action'];

$name = $_POST['form'][0]['name'];
$email = $_POST['form'][0]['email'];
$subject = 'Contacto desde www.leoleiva.ar';
$message = $_POST['form'][0]['message'];
$mensaje = "
<table border='0' cellspacing='3' cellpadding='2'>
<tr>
<td width='30%' align='left' bgcolor='#f0efef'><strong>Nombre:</strong></td>
<td width='80%' align='left'>$name</td>
</tr>
<tr>
<td align='left' bgcolor='#f0efef'><strong>E-mail:</strong></td>
<td align='left'>$email</td>
</tr>
<tr>
<td align='left' bgcolor='#f0efef'><strong>Comentario:</strong></td>
<td align='left'>$message</td>
</tr>
</table>
";

if ($name == "") {
    echo "<p class=\"error\">Por favor complete su nombre</p>";
} else if ($email == "") {
    echo "<p class=\"error\">Por favor complete su email</p>";
} else if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    echo "<p class=\"error\">Formato de e-mail inválido</p>";
} else if ($message == "") {
    echo "<p class=\"error\">Por favor complete su mensaje</p>";
} else if (!preg_match("/^[a-zA-Z ]*$/", $name)) {
    echo "<p class=\"error\">Solo se permiten letras y espacios en blanco en el nombre</p>";
} else {
    $header = "From: $name <$email>\r\n"; //Quien envia?
    $header .= "X-Mailer: PHP5\n";
    $header .= 'MIME-Version: 1.0' . "\n";
    $header .= 'Content-type: text/html; charset=iso-8859-1' . "\r\n"; //


    //Comprobamos que los datos enviados a la función MAIL de PHP estén bien y si es correcto enviamos
    if (mail($sendTo, $subject, $mensaje, $header)) {
        echo "<p class=\"success\">Mensaje enviado correctamente.<br>Muchas gracias</p>";
    } else {
        echo "<p class=\"error\">Hubo un problema al enviar el E-Mail.</p>";
    }
}
