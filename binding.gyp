{
  # NOTE: 'module_name' and 'module_path' come from the 'binary' property in package.json
  # node-pre-gyp handles passing them down to node-gyp when you build from source
  "targets": [
    {
      "target_name": "action_install",
      "type": "none",
      "actions": [
        {
          "action_name": "echo_message",
          "action": [
            "echo",
            "'No target needed to build!'"
          ]
        }
      ]
    }

    # {
    #   "target_name": "<(module_name)",
    #   "sources": [ "binding.cpp" ],
    # },
    # {
    #   "target_name": "action_after_build",
    #   "type": "none",
    #   "dependencies": [ "<(module_name)" ],
    #   "copies": [
    #     {
    #       "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
    #       "destination": "<(module_path)"
    #     }
    #   ]
    # }
  ]
}
