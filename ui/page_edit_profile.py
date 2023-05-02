import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog
from PIL import Image
from io import BytesIO
import re, os, base64

from ui.components.image_view import ImageView
from ui.components.temed_components import ThemedButton, ThemedEntry
from utils.minecraft_profiles_helper import MCProfile

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ui.app import App

class PageEditProfile(ctk.CTkFrame):
    def __init__(self, app: "App", profile: MCProfile = None):
        super().__init__(app, fg_color="transparent")
        self.app = app

        self.existing_profile = profile is not None
        self.profile = profile if self.existing_profile else MCProfile("", "", "", "")

        fv_content = ctk.CTkFrame(self, fg_color="transparent")

        self.iv_profile_icon = ImageView(fv_content, None, size=(100, 100), radius=20)
        self.iv_profile_icon.grid(row=0, column=0, rowspan=2)
        if self.existing_profile:
            self.iv_profile_icon.set_image(self.profile.get_icon())
        else:
            self.iv_profile_icon.set_image(Image.open(os.path.join(self.app.ROOT_DIR, "assets", "profile_icons", "default_profile_icon.png")))

        self.bt_upload_icon = ThemedButton(fv_content, text="Upload Icon", font_size=20, border_spacing=10, command=self._upload_icon)
        self.bt_upload_icon.grid(row=2, column=0, padx=10, pady=10)

        self.et_profile_name = ThemedEntry(fv_content, font_size=25, width=300)
        self.et_profile_name.insert(0, self.profile.profile_name)
        self.et_profile_name.bind("<KeyRelease>", self._update_id)
        self.et_profile_name.grid(row=0, column=1, padx=10, pady=10)

        self.et_profile_id = ThemedEntry(fv_content, enabled=False, font_size=20, width=300)
        self.et_profile_id.insert(0, self.profile.profile_id)
        self.et_profile_id.grid(row=1, column=1, padx=10, pady=10)

        fv_content.pack(padx=30, pady=30, fill=tk.BOTH, expand=True)

        fv_apply = ctk.CTkFrame(self, fg_color="transparent")

        bt_cancel = ThemedButton(fv_apply, text="Cancel", font_size=20, border_spacing=10, command=self._back)
        bt_cancel.pack(side=tk.LEFT, padx=10)

        bt_save = ThemedButton(fv_apply, text="Save", font_size=20, primary=True, border_spacing=10, command=self._save)
        bt_save.pack(side=tk.RIGHT)

        fv_apply.place(relx=1, rely=1, anchor="se", x=-30, y=-30)

    def _upload_icon(self):
        icon_path = filedialog.askopenfilename(initialdir=os.path.join(self.app.ROOT_DIR, "assets", "profile_icons"), title="Select Icon")
        if icon_path is None: return

        icon = Image.open(icon_path)
        self.iv_profile_icon.set_image(icon)

    def _update_id(self, event):
        if self.existing_profile: return

        new_id = self.et_profile_name.get()
        new_id = new_id.lower().replace(" ", "-")
        new_id = "".join([c for c in new_id if re.match(r"[a-z0-9\-\.]", c) is not None])

        self.et_profile_id.configure(state=tk.NORMAL)
        self.et_profile_id.delete(0, tk.END)
        self.et_profile_id.insert(0, new_id)
        self.et_profile_id.configure(state=tk.DISABLED)

    def _save(self):
        icon_image = self.iv_profile_icon.get_image().resize((128, 128), Image.ANTIALIAS)

        icon_buffer = BytesIO()
        icon_image.save(icon_buffer, format="PNG")
        icon_base64 = "data:image/png;base64," + base64.b64encode(icon_buffer.getvalue()).decode("utf-8")

        self.app.advanced_profile_helper.set_profile(
            self.app.mc_profile_helper,
            MCProfile(
                self.et_profile_id.get(),
                icon_base64,
                self.et_profile_name.get(),
                "" # VERSION
            ),
            [], # MODS
            [], # RESOURCE PACKS
            "" # JAVA ARGS
        )

        from ui.page_profiles_list import PageProfilesList
        self.app.navigate(PageProfilesList)

    def _back(self):
        from ui.page_profiles_list import PageProfilesList
        self.app.navigate(PageProfilesList)