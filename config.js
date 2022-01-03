function save_config_data (json_object) {


  password_input = document.querySelector("#password_set_input").value;
  json_object.password = password_input

  // json_object = {
  //   password: password_input,
  //   shortcuts: {
  //     windows: {
  //       keyboard_shortcut: {
  //         h: "shift+H",
  //         up: "ctrl+up",
  //       },
  //       sequence: {},
  //       open_app: {},
  //       write_text: {},
  //     },
  //     macos: {
  //       keyboard_shortcut: {
  //         spotlight: "command+space",
  //       },
  //     },
  //     linux: {
  //       open_app: {},
  //     },
  //   },
  // };



  platforms_list = Object.keys(json_object["shortcuts"])
  for (i=0; i < platforms_list.length; i++) {
    current_platform = platforms_list[i]
    for (j=0; j < json_object["shortcuts"][current_platform]; j++) {
      current_action_type = son_object["shortcuts"][current_platform][j]

      k=0
      while (true) {
        try {
          item_name = document.querySelector(`#${current_platform}__${current_action_type}__name__${k}`).value;
          item_shortcut = document.querySelector(`#${current_platform}__${current_action_type}__shortcut__${k}`).value;
        } catch (e) {
          break
        }
        json_object["shortcuts"][current_platform][current_action_type][item_name] = item_shortcut
        k++



      }
    }
  }
  console.log(json_object);
}
