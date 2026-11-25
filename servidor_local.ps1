$ErrorActionPreference = "Stop"
$root = (Resolve-Path $PSScriptRoot).Path
$listener = New-Object System.Net.HttpListener
$prefix = "http://127.0.0.1:8765/"
$listener.Prefixes.Add($prefix)
try {
    $listener.Start()
    Start-Process $prefix
    Write-Host "`nSimulador ativo em $prefix" -ForegroundColor Green
    Write-Host "Mantenha esta janela aberta enquanto usar o simulador. Para encerrar, pressione Ctrl+C."
    while ($listener.IsListening) {
        $context = $listener.GetContext()
        try {
            $relative = [Uri]::UnescapeDataString($context.Request.Url.AbsolutePath.TrimStart('/'))
            if ([string]::IsNullOrWhiteSpace($relative)) { $relative = "index.html" }
            $relative = $relative.Replace('/', [IO.Path]::DirectorySeparatorChar)
            $file = [IO.Path]::GetFullPath((Join-Path $root $relative))
            if (-not $file.StartsWith($root, [StringComparison]::OrdinalIgnoreCase) -or -not (Test-Path -LiteralPath $file -PathType Leaf)) {
                $context.Response.StatusCode = 404
                $bytes = [Text.Encoding]::UTF8.GetBytes("404 - Arquivo nao encontrado")
            } else {
                $ext = [IO.Path]::GetExtension($file).ToLowerInvariant()
                $context.Response.ContentType = switch ($ext) {
                    ".html" { "text/html; charset=utf-8" }
                    ".js" { "text/javascript; charset=utf-8" }
                    ".css" { "text/css; charset=utf-8" }
                    ".glb" { "model/gltf-binary" }
                    ".gltf" { "model/gltf+json" }
                    default { "application/octet-stream" }
                }
                $bytes = [IO.File]::ReadAllBytes($file)
                $context.Response.StatusCode = 200
            }
            $context.Response.ContentLength64 = $bytes.Length
            $context.Response.OutputStream.Write($bytes, 0, $bytes.Length)
        } catch { $context.Response.StatusCode = 500 }
        finally { $context.Response.OutputStream.Close() }
    }
} finally { $listener.Stop(); $listener.Close() }
