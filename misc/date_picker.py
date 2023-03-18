# Credit @Tensor - https://discord.com/channels/736279277242417272/1083377856064798781/1086329311532953652
import threading
import traceback
from datetime import datetime, timedelta
from functools import cache
from typing import Callable, Self

import dearpygui.dearpygui as dpg
from dateutil.relativedelta import relativedelta


class call_when_dpg_running:
    dpg_running = False
    worker_started = False
    queue = []

    def __new__(cls, func):
        def decorator(*args, **kwargs):
            if not cls.worker_started:
                cls.worker_started = True
                threading.Thread(target=cls._worker, daemon=True).start()

            if cls.dpg_running:
                func(*args, **kwargs)
            else:
                cls.queue.append((func, args, kwargs))

        return decorator

    @classmethod
    def _worker(cls):
        while dpg.get_frame_count() < 1:
            dpg.split_frame(delay=0)
        cls.dpg_running = True
        for data in cls.queue:
            func, args, kwargs = data
            try:
                func(*args, **kwargs)
            except Exception:
                traceback.print_exc()
        del cls.queue


def cached_class_attr(f):
    return property(cache(f))


class DatePicker:
    weekdays = ('Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa')
    months = (
        '1-January', '2-February',
        '3-March', '4-April', '5-May',
        '6-June', '7-July', '8-August',
        '9-September', '10-October', '11-November',
        '12-December',
    )

    callback: Callable[[datetime], None] = None

    date: datetime
    min_value: datetime = datetime(year=1970, month=1, day=1)
    max_value: datetime = datetime(year=2999, month=12, day=31)

    group: int
    _selected_day_tag: int = None

    @classmethod
    @cached_class_attr
    def _theme(cls) -> int:
        with dpg.theme() as theme:
            with dpg.theme_component(dpg.mvAll, parent=theme) as theme_component:
                dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (0, 0, 0, 0), category=dpg.mvThemeCat_Core, parent=theme_component)
                dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 0, 0, category=dpg.mvThemeCat_Core, parent=theme_component)
                dpg.add_theme_style(dpg.mvStyleVar_CellPadding, 0, 0, category=dpg.mvThemeCat_Core, parent=theme_component)
                cls._frame_padding = dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 4, 3, category=dpg.mvThemeCat_Core, parent=theme_component)
            with dpg.theme_component(dpg.mvButton, parent=theme) as theme_component:
                dpg.add_theme_color(dpg.mvThemeCol_Button, (0, 0, 0, 0), category=dpg.mvThemeCat_Core, parent=theme_component)
            with dpg.theme_component(dpg.mvButton, enabled_state=False, parent=theme) as theme_component:
                dpg.add_theme_style(dpg.mvStyleVar_Alpha, 0.3, category=dpg.mvThemeCat_Core, parent=theme_component)
                dpg.add_theme_color(dpg.mvThemeCol_Button, (0, 0, 0, 0), category=dpg.mvThemeCat_Core, parent=theme_component)
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (0, 0, 0, 0), category=dpg.mvThemeCat_Core, parent=theme_component)
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (0, 0, 0, 0), category=dpg.mvThemeCat_Core, parent=theme_component)
            with dpg.theme_component(dpg.mvInputInt, enabled_state=False, parent=theme) as theme_component:
                dpg.add_theme_style(dpg.mvStyleVar_Alpha, 0.75, category=dpg.mvThemeCat_Core, parent=theme_component)
                dpg.add_theme_color(dpg.mvThemeCol_TextSelectedBg, (0, 0, 0, 0), category=dpg.mvThemeCat_Core, parent=theme_component)
            with dpg.theme_component(dpg.mvCombo, enabled_state=False, parent=theme) as theme_component:
                dpg.add_theme_style(dpg.mvStyleVar_Alpha, 0.75, category=dpg.mvThemeCat_Core, parent=theme_component)
                dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, (0, 0, 0, 0), category=dpg.mvThemeCat_Core, parent=theme_component)
                dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (0, 0, 0, 0), category=dpg.mvThemeCat_Core, parent=theme_component)
        return theme

    @classmethod
    @cached_class_attr
    def _weekdays_theme(cls) -> int:
        with dpg.theme() as theme:
            with dpg.theme_component(parent=theme) as theme_component:
                dpg.add_theme_color(dpg.mvThemeCol_Button, (0, 0, 0, 0), category=dpg.mvThemeCat_Core, parent=theme_component)
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (0, 0, 0, 0), category=dpg.mvThemeCat_Core, parent=theme_component)
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (0, 0, 0, 0), category=dpg.mvThemeCat_Core, parent=theme_component)
        return theme

    @classmethod
    @cached_class_attr
    def _selected_day_theme(cls) -> int:
        with dpg.theme() as theme:
            with dpg.theme_component(parent=dpg.mvButton) as theme_component:
                # Set the background color of your choice here
                dpg.add_theme_color(dpg.mvThemeCol_Button, (51, 51, 55, 255), category=dpg.mvThemeCat_Core, parent=theme_component)
        return theme

    @classmethod
    @cached_class_attr
    def _another_month_day_theme(cls) -> int:
        with dpg.theme() as theme:
            with dpg.theme_component(parent=dpg.mvButton) as theme_component:
                dpg.add_theme_style(dpg.mvStyleVar_Alpha, 0.5, category=dpg.mvThemeCat_Core, parent=theme_component)
        return theme

    def __init__(self, date: datetime = None, callback: Callable[[datetime], None] = None):
        if date is None:
            date = datetime.now()
        self.date = datetime(date.year, date.month, date.day)
        self.callback = callback

        with dpg.group(width=100) as self.group:
            dpg.bind_item_theme(self.group, self._theme)
            with dpg.table(header_row=False, parent=self.group) as self._month_days_table:
                dpg.add_table_column(parent=self._month_days_table)
                dpg.add_table_column(width_fixed=True, parent=self._month_days_table)
                dpg.add_table_column(width_fixed=True, parent=self._month_days_table)

                with dpg.table_row(parent=self._month_days_table) as table_row:
                    with dpg.group(horizontal=True, parent=table_row) as group:
                        self.month_combo = dpg.add_combo(items=self.months, default_value=self.months[self.date.month - 1],
                                                         parent=group, no_arrow_button=True,
                                                         callback=lambda _, month_name: self._click_month(self.months.index(month_name)))
                        self.year_input = dpg.add_input_int(default_value=self.date.year, step=0, step_fast=0,
                                                            parent=group,
                                                            callback=lambda _, year: self._click_year(year))
                    self.past_month_button = dpg.add_button(arrow=True, direction=dpg.mvDir_Left,
                                                            parent=table_row,
                                                            callback=lambda: self._click_month('-'))
                    self.next_month_button = dpg.add_button(arrow=True, direction=dpg.mvDir_Right,
                                                            parent=table_row,
                                                            callback=lambda: self._click_month('+'))

            with dpg.group():
                with dpg.table(header_row=False, policy=dpg.mvTable_SizingFixedFit,
                               parent=self.group) as self._month_days_table:
                    for _ in range(7):
                        dpg.add_table_column(parent=self._month_days_table)

        self._refresh_all()

    def _do_callback(self):
        if self.callback is None:
            return
        try:
            self.callback(self.date)
        except Exception:
            traceback.print_exc()

    def _set_selected_day_tag(self, tag: int):
        try:
            dpg.bind_item_theme(self._selected_day_tag, 0)
        except Exception:
            pass
        finally:
            self._selected_day_tag = tag
            dpg.bind_item_theme(tag, self._selected_day_theme)

    @call_when_dpg_running
    def _refresh_all(self):
        self._refresh_month_and_year()
        self._refresh_month_days()

        width = dpg.get_text_size("  ".join(self.weekdays) + "  ")[0] + dpg.get_value(self._frame_padding)[0] * 7 * 2
        dpg.set_item_width(self.group, width)

    def _refresh_month_and_year(self):
        dpg.set_value(self.year_input, self.date.year)

        available_months = self.months
        if self.date.year == self.max_value.year:
            available_months = available_months[:self.max_value.month:]
        if self.date.year == self.min_value.year:
            available_months = available_months[self.min_value.month - 1::]

        month_name = self.months[self.date.month - 1]
        dpg.configure_item(self.month_combo, default_value=month_name, items=available_months,
                           width=dpg.get_text_size(month_name)[0] + dpg.get_value(self._frame_padding)[0] * 2)

        enabled_month_combo = True
        if self.min_value.month == self.max_value.month and self.min_value.year == self.max_value.year:
            enabled_month_combo = False
        dpg.configure_item(self.month_combo, enabled=enabled_month_combo)

        enabled_year_input = True
        if self.min_value.year == self.max_value.year:
            enabled_year_input = False
        dpg.configure_item(self.year_input, enabled=enabled_year_input)

        enabled_next_month_btn = True
        if self.date.month + 1 > self.max_value.month and self.date.year == self.max_value.year:
            enabled_next_month_btn = False
        dpg.configure_item(self.next_month_button, enabled=enabled_next_month_btn)

        enabled_past_month_btn = True
        if self.date.month - 1 < self.min_value.month and self.date.year == self.min_value.year:
            enabled_past_month_btn = False
        dpg.configure_item(self.past_month_button, enabled=enabled_past_month_btn)

    def _refresh_month_days(self):
        dpg.delete_item(self._month_days_table, children_only=True, slot=1)

        with dpg.table_row(parent=self._month_days_table):
            for i in range(7):
                btn = dpg.add_button(label=f" {self.weekdays[i]} ")
                dpg.bind_item_theme(btn, self._weekdays_theme)

        start_date = self.date.replace(day=1)
        start_date -= timedelta(days=start_date.weekday())
        start_date -= timedelta(days=1)
        for _ in range(6):  # rows count
            with dpg.table_row(parent=self._month_days_table) as table_row:
                for _ in range(7):
                    start_date += timedelta(days=1)
                    if start_date < self.min_value or start_date > self.max_value:
                        dpg.add_text(parent=table_row)
                        continue

                    user_data = f"{start_date.day}"
                    if start_date.month != self.date.month:
                        if start_date < self.date:
                            user_data = f"-{user_data}"
                        else:
                            user_data = f"+{user_data}"

                    btn = dpg.add_button(label=f"{start_date.day}", width=-1, parent=table_row,
                                         user_data=user_data, callback=self._click_month_day)

                    if start_date.month != self.date.month:
                        dpg.bind_item_theme(btn, self._another_month_day_theme)
                    elif start_date.day == self.date.day:
                        self._set_selected_day_tag(btn)

    def _click_month_day(self, btn: int | str, _, day: str):
        if day[0] in ('+', '-'):
            self.date = self.date.replace(day=1)
            if day[0] == '+':
                self.date += relativedelta(months=1)
            else:
                self.date -= relativedelta(months=1)
            self.date = self.date.replace(day=int(day[1:]))

            self._refresh_all()
        else:
            self.date = self.date.replace(day=int(day))
            self._set_selected_day_tag(btn)
        self._do_callback()

    def _click_month(self, month: str | int):
        if month == '+':
            self.date += relativedelta(months=1)
        elif month == '-':
            self.date += relativedelta(months=-1)
        else:
            month = int(month) + 1
            self.date += relativedelta(months=month - self.date.month)

        if self.date > self.max_value:
            self.date = self.max_value
        elif self.date < self.min_value:
            self.date = self.min_value

        self._refresh_all()
        self._do_callback()

    def _click_year(self, year: int):  # click?
        if not (len(str(self.min_value.year)) <= len(str(year)) <= len(str(self.max_value.year))):
            dpg.set_value(self.year_input, self.date.year)
            return

        if year < self.min_value.year:
            year = self.min_value.year
        elif year > self.max_value.year:
            year = self.max_value.year

        if year == self.date.year:
            dpg.set_value(self.year_input, self.date.year)
            return

        date_with_new_year = self.date.replace(year=year)
        if date_with_new_year < self.min_value:
            self.date = self.min_value
        elif date_with_new_year > self.max_value:
            self.date = self.max_value
        else:
            self.date = date_with_new_year
        self._refresh_all()
        self._do_callback()

    def set_min_value(self, min_limit: datetime) -> Self:
        if min_limit > self.max_value:
            raise ValueError("`min_limit` must be less than `max_limit`")
        self.min_value = min_limit
        if self.date < self.min_value:
            self.date = self.min_value
        self._refresh_all()
        return self

    def set_max_value(self, max_limit: datetime) -> Self:
        if max_limit < self.min_value:
            raise ValueError("`max_limit` must be greater than `min_limit`")
        self.max_value = max_limit
        if self.date > self.max_value:
            self.date = self.max_value
        self._refresh_all()
        return self

    def set_value(self, date: datetime) -> Self:
        date = datetime(date.year, date.month, date.day)
        if date > self.max_value:
            raise ValueError("`date` must be less than `max_limit`")
        if date < self.min_value:
            raise ValueError("`date` must be greater than `min_limit`")
        self.date = date
        self._refresh_all()
        return self

    def get_value(self) -> datetime:
        return self.date


if __name__ == '__main__':
    dpg.create_context()
    dpg.create_viewport()

    with dpg.window() as window:
        dpg_text = dpg.add_text()
        date_picker = DatePicker(callback=lambda date, *, _dpg_text=dpg_text: dpg.set_value(_dpg_text, date))
        dpg.set_value(dpg_text, date_picker.get_value())

        dpg_text = dpg.add_text()
        date_picker = DatePicker(callback=lambda date, *, _dpg_text=dpg_text: dpg.set_value(_dpg_text, date)) \
            .set_min_value(datetime(2021, 3, 4)) \
            .set_max_value(datetime(2022, 9, 15)) \
            .set_value(datetime(2021, 8, 2))
        dpg.set_value(dpg_text, date_picker.get_value())

        dpg_text = dpg.add_text()
        date_picker = DatePicker(callback=lambda date, *, _dpg_text=dpg_text: dpg.set_value(_dpg_text, date)) \
            .set_min_value(datetime(2021, 5, 10)) \
            .set_max_value(datetime(2021, 8, 25)) \
            .set_value(datetime(2021, 7, 8))
        dpg.set_value(dpg_text, date_picker.get_value())

        dpg_text = dpg.add_text()
        date_picker = DatePicker(callback=lambda date, *, _dpg_text=dpg_text: dpg.set_value(_dpg_text, date)) \
            .set_min_value(datetime(2020, 8, 10)) \
            .set_max_value(datetime(2020, 8, 25)) \
            .set_value(datetime(2020, 8, 15))
        dpg.set_value(dpg_text, date_picker.get_value())

    dpg.set_primary_window(window, True)

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()