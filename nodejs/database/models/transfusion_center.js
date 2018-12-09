'use strict';

module.exports = (sequelize, DataTypes) => {
    const transfusion_center = sequelize.define('transfusion_center', {
        id_center: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            autoIncrement: true
        },
        name: {
            type: DataTypes.STRING(50),
        }
    }, {
        freezeTableName: true,
        timestamps: false,
        underscored: true,
        name: {
            singular: 'transfusion_center',
            plural: 'transfusion_center'
        }
    });

    transfusion_center.associate = models => {
        transfusion_center.hasMany(models.request, {
            foreignKey: 'id_center',
            onDelete: 'cascade'
        });

        transfusion_center.hasMany(models.employee, {
            foreignKey: 'id_center',
            onDelete: 'cascade'
        });
    };

    return transfusion_center;
};
