{
  "targets": [
    {
      "target_name": "wkhtmltopdf",
      "sources": [ "wkhtmltopdf.cc" ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
        "lib/wkhtmltopdf/src/lib",
        "lib/wkhtmltopdf/src/pdf"
      ]
    }
  ]
}
