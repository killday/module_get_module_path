from odoo import api, fields, models
from odoo.modules.module import get_module_path
import os

class IrModuleModule(models.Model):
    _inherit = 'ir.module.module'

    folder_name = fields.Char(compute='_compute_folder_name', store=True)

    def _compute_folder_name(self):
        for record in self:
            module_path = get_module_path(record.name)

            if module_path:
                # Split the path into a list of directories
                path_parts = module_path.split(os.sep)
                if len(path_parts) > 1:
                        record.folder_name = path_parts[-2]
                