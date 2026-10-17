Add-Type -AssemblyName System.Drawing

$width = 1200
$height = 630
$bmp = [System.Drawing.Bitmap]::new($width, $height)
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::ClearTypeGridFit
$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic

# Fundo escuro com gradiente elegante
$rect = [System.Drawing.Rectangle]::new(0, 0, $width, $height)
$c1 = [System.Drawing.ColorTranslator]::FromHtml("#05070F")
$c2 = [System.Drawing.ColorTranslator]::FromHtml("#0C172B")
$brushBg = [System.Drawing.Drawing2D.LinearGradientBrush]::new($rect, $c1, $c2, 45.0)
$g.FillRectangle($brushBg, $rect)

# Detalhe sutil de borda ciano
$penBorder = [System.Drawing.Pen]::new([System.Drawing.ColorTranslator]::FromHtml("#1B2E4B"), 2)
$g.DrawRectangle($penBorder, 1, 1, ($width - 2), ($height - 2))

# Brilho de circuito no topo/esquerda
$penCyan = [System.Drawing.Pen]::new([System.Drawing.ColorTranslator]::FromHtml("#22D3EE"), 3)
$g.DrawLine($penCyan, 80, 48, 220, 48)

# Carregar Logo
$logoPath = "c:\Users\lamacedo\Documents\Antigravity\Infohausti\logo.jpg"
if (Test-Path $logoPath) {
    $logoBmp = [System.Drawing.Image]::FromFile($logoPath)
    $logoRect = [System.Drawing.Rectangle]::new(80, 75, 96, 96)
    $g.DrawImage($logoBmp, $logoRect)
    $logoBmp.Dispose()
    
    # Borda em volta da logo
    $penLogo = [System.Drawing.Pen]::new([System.Drawing.ColorTranslator]::FromHtml("#22D3EE"), 2)
    $g.DrawRectangle($penLogo, 79, 74, 98, 98)
}

# Caracteres com escape Unicode 100% à prova de codepage
$o_til = [char]0x00F3   # ó
$e_agudo = [char]0x00E9 # é
$a_til = [char]0x00E3   # ã
$a_agudo = [char]0x00E1 # á
$c_cedilha = [char]0x00C7 # Ç
$a_til_M = [char]0x00C3   # Ã
$bullet = [char]0x2022    # •

# Texto INFOHAUS TI
$fontBrand = [System.Drawing.Font]::new("Segoe UI", [float]26, [System.Drawing.FontStyle]::Bold)
$fontTag = [System.Drawing.Font]::new("Segoe UI", [float]11, [System.Drawing.FontStyle]::Bold)
$brushWhite = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::White)
$brushCyan = [System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml("#22D3EE"))
$brushMuted = [System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml("#9AA5B8"))

$g.DrawString("INFOHAUS", $fontBrand, $brushWhite, 196, 82)
$g.DrawString(" TI", $fontBrand, $brushCyan, 362, 82)

$subBrand = "TECNOLOGIA & PRESEN" + $c_cedilha + "A DIGITAL " + $bullet + " RIBEIR" + $a_til_M + "O PRETO/SP"
$g.DrawString($subBrand, $fontTag, $brushMuted, 198, 130)

# Título Principal
$fontTitle = [System.Drawing.Font]::new("Segoe UI", [float]38, [System.Drawing.FontStyle]::Bold)
$titleText = "Seu neg" + $o_til + "cio aparece quando algu" + $e_agudo + "m busca no Google em Ribeir" + $a_til + "o Preto?"
$titleRect = [System.Drawing.RectangleF]::new(80, 215, 1040, 225)
$format = [System.Drawing.StringFormat]::new()
$format.LineAlignment = [System.Drawing.StringAlignment]::Near
$format.Alignment = [System.Drawing.StringAlignment]::Near
$g.DrawString($titleText, $fontTitle, $brushWhite, $titleRect, $format)

# Caixa de destaque inferior (Pill de Conversão)
$pillRect = [System.Drawing.Rectangle]::new(80, 480, 1040, 84)
$pillBg = [System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml("#0E1B33"))
$g.FillRectangle($pillBg, $pillRect)
$pillPen = [System.Drawing.Pen]::new([System.Drawing.ColorTranslator]::FromHtml("#22D3EE"), 2)
$g.DrawRectangle($pillPen, $pillRect)

$fontPillBold = [System.Drawing.Font]::new("Segoe UI", [float]15, [System.Drawing.FontStyle]::Bold)
$fontPillSub = [System.Drawing.Font]::new("Segoe UI", [float]13, [System.Drawing.FontStyle]::Regular)

$pillHeader = "OTIMIZA" + $c_cedilha + $a_til_M + "O DO PERFIL DA EMPRESA NO GOOGLE"
$pillText = "An" + $a_agudo + "lise gratuita do seu perfil pelo WhatsApp: (16) 98146-9121"

$g.DrawString($pillHeader, $fontPillBold, $brushCyan, 110, 495)
$g.DrawString($pillText, $fontPillSub, $brushWhite, 110, 528)

# Salvar JPEG com qualidade 95
$outputPath = "c:\Users\lamacedo\Documents\Antigravity\Infohausti\perfil-google\og.jpg"
$encoderParams = [System.Drawing.Imaging.EncoderParameters]::new(1)
$encoderParams.Param[0] = [System.Drawing.Imaging.EncoderParameter]::new([System.Drawing.Imaging.Encoder]::Quality, 95L)
$jpegCodec = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq "image/jpeg" }

$bmp.Save($outputPath, $jpegCodec, $encoderParams)
$g.Dispose()
$bmp.Dispose()

Write-Output "Criado com sucesso: $outputPath (Tamanho: $((Get-Item $outputPath).Length) bytes)"
