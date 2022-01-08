'use strict';

function save_config_data(json_object) {


    json_object.password = document.querySelector("#password_set_input").value

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


    let platforms_list = Object.keys(json_object["shortcuts"])
    let current_platform;
    let current_action_type;
    let k;
    let item_name;
    let item_shortcut;
    for (let i = 0; i < platforms_list.length; i++) {
        current_platform = platforms_list[i]
        for (let j = 0; j < Object.keys(json_object["shortcuts"][current_platform]).length; j++) {
            current_action_type = json_object["shortcuts"][current_platform][j]

            k = 0
            while (true) {
              console.log('hi')
                // try {
                    item_name = document.querySelector(`#${current_platform}__${current_action_type}__name__${k}`).value;
                    item_shortcut = document.querySelector(`#${current_platform}__${current_action_type}__shortcut__${k}`).value;
                // } catch (e) {
                    while (true) {
                        // try {
                            item_name = document.querySelector(`#${current_platform}__${current_action_type}__name__${k}__new`).value;
                            item_shortcut = document.querySelector(`#${current_platform}__${current_action_type}__shortcut__${k}__new`).value;
                        // } catch (e) {
                        //     break
                        // }
                        json_object["shortcuts"][current_platform][current_action_type][item_name] = item_shortcut
                      console.log(item_name, item_shortcut, json_object["shortcuts"][current_platform][current_action_type][item_name])
                        k++
                    }
                    // break
                // }
                json_object["shortcuts"][current_platform][current_action_type][item_name] = item_shortcut
                k++


            }
        }
    }
    console.log(json_object);
}
