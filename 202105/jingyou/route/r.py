from flask import request, render_template, redirect, url_for, flash, session
from sqlalchemy import and_, or_
############################################
# 路由
############################################
from jingyou import app
from jingyou.model.User import User
from jingyou.model.Oil import Oil




