{
  # NOTE: 'module_name' and 'module_path' come from the 'binary' property in package.json
  # node-pre-gyp handles passing them down to node-gyp when you build from source
  "targets": [
    {
      "target_name": "action_install",
      "type": "none",
      "actions": [
        {
          "action_name": "build_from_source",
          "inputs": [],
          "outputs": [ "/dev/null" ],
          "action": [
            "./lib/wkhtmltopdf/scripts/build.py",
            "osx-cocoa-x86-64"
          ]
        }
      ]
    }
  ]
}
