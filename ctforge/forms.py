#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, HiddenField, IntegerField, BooleanField, TextAreaField, validators

class LoginForm(FlaskForm):
    mail = StringField('mail', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.DataRequired()])

class ServiceFlagForm(FlaskForm):
    team_token = HiddenField('team_token', validators=[validators.DataRequired()])
    flag = StringField('flag', validators=[validators.DataRequired()])

class ChallengeFlagForm(FlaskForm):
    flag = StringField('flag', validators=[validators.DataRequired()])

class ServiceForm(FlaskForm):
    name = StringField('name', validators=[validators.DataRequired()])
    description = TextAreaField('description', validators=[validators.DataRequired()])
    active = BooleanField('active')

class ChallengeForm(FlaskForm):
    name = StringField('name', validators=[validators.DataRequired()])
    description = TextAreaField('description', validators=[validators.DataRequired()])
    flag = StringField('flag', validators=[validators.DataRequired()])
    points = IntegerField('points', validators=[validators.NumberRange(message='Challenge points should be between 0 and 1000.', min=0, max=1000)])
    active = BooleanField('active')
    writeup = BooleanField('writeup')
    writeup_template = TextAreaField('writeup_template')

class ChallengeWriteupForm(FlaskForm):
    writeup = TextAreaField('writeup', validators=[validators.DataRequired()])

class AdminWriteupForm(FlaskForm):
    mail = StringField('mail', render_kw={'disabled': True})
    name = StringField('name', render_kw={'disabled': True})
    surname = StringField('surname', render_kw={'disabled': True})
    challenge = StringField('challenge', render_kw={'disabled': True})
    timestamp = StringField('timestamp', render_kw={'disabled': True})
    writeup = TextAreaField('writeup', render_kw={'disabled': True})
    grade = IntegerField('grade', validators=[validators.Optional(), validators.NumberRange(message='Grade should be between 0 and 10.', min=0, max=10)])
    feedback = TextAreaField('feedback')

class ManualForm(FlaskForm):
    team_id = IntegerField('team_id', validators=[validators.DataRequired()])
    chal_id = IntegerField('Challenge Number')

    level = IntegerField('What level of points would you like to take away from the team for the hints? Take a percentage based upon the guideline.',
    validators=[validators.DataRequired(),validators.NumberRange(message='Deduction should be between 1 and 5.', min=1, max=5)])

class FixForm(FlaskForm):
    team_id = IntegerField('team_id', validators=[validators.DataRequired()])
    points = IntegerField('Set hint value to: ')
    remember_me = StringField("Remember, this will set the teams hint value to EXACTLY what is in the points field. So, be careful. Put anything in here to validate this...", validators=[validators.DataRequired()])

class UserForm(FlaskForm):
    team_id = IntegerField('team_id', validators=[validators.Optional()])
    name = StringField('name', validators=[validators.DataRequired()])
    surname = StringField('surname', validators=[])
    mail = StringField('mail', validators=[validators.DataRequired()])
    password = StringField('password')
    admin = BooleanField('admin')
    hidden = BooleanField('hidden')

class TeamForm(FlaskForm):
    ip = StringField('ip', validators=[validators.DataRequired()])
    name = StringField('name', validators=[validators.DataRequired()])
    token = StringField('token', validators=[validators.DataRequired()])
    poc = IntegerField('poc', validators=[validators.Optional()])
