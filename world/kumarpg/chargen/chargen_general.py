from world.utilities.format import wrap, header
from django.conf import settings
from world.kumarpg.chargen.chargen_template import node_package, node_view_pregen, _set_template
from world.kumarpg.chargen.chargen_weapons import node_weapons, node_weapons_2, _reset_weapons, _set_weapon
from world.kumarpg.chargen.chargen_skills import node_skills, _reset_skills, _set_skill
from world.kumarpg.chargen.chargen_utils import cgen_header


def node_start(_):
    text = "Welcome to the |w{}|n character generation system. There" \
           "are two options for going through character generation. 1. Choose" \
           "a pregen template and personalize it.  Or 2. Build your own sheet" \
           "from scratch (advanced)." \
        .format(settings.SERVERNAME)

    options = (
        {
            "key": ("Pregen", "pregen", "pre"),
            "desc": "Start with a pre-generated template",
            "goto": "node_package"
        }
    )

    return cgen_header("The Beginning") + "\n" + wrap(text, indent=1), options
