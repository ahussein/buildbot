# This file is part of Buildbot.  Buildbot is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright Buildbot Team Members

import sqlalchemy as sa

def upgrade(migrate_engine):
    metadata = sa.MetaData()
    metadata.bind = migrate_engine

    # add project and repository columns to 'changes' an 'sourcestamps'
    def add_cols(table):
        repository = sa.Column('repository', sa.Text, nullable=False, server_default=sa.DefaultClause(''))
        repository.create(table, populate_default=True)
        project = sa.Column('project', sa.Text, nullable=False, server_default=sa.DefaultClause(''))
        project.create(table, populate_default=True)

    add_cols(sa.Table('changes', metadata, autoload=True))
    add_cols(sa.Table('sourcestamps', metadata, autoload=True))
