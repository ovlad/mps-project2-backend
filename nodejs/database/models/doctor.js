'use strict';

module.exports = (sequelize, DataTypes) => {
    const doctor = sequelize.define('doctor', {
        id_doctor: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            autoIncrement: true
        },
        name: {
            type: DataTypes.STRING(30),
        },
        surname: {
            type: DataTypes.STRING(30),
        },
        mail: {
            type: DataTypes.STRING(30),
        },
        password: {
            type: DataTypes.STRING(30),
        },
        is_active: {
            type: DataTypes.BOOLEAN,
            defaultValue: false
        },
        id_hospital: {
                type: DataTypes.INTEGER
        }
    }, {
        freezeTableName: true,
        underscored: true,
        name: {
            singular: 'doctor',
            plural: 'doctor'
        }
    });

    doctor.associate = models => {
        doctor.belongsTo(models.hospital, {
            foreignKey: 'id_hospital'
        });

        doctor.hasMany(models.request, {
            foreignKey: 'id_doctor',
            onDelete: 'cascade'
        });
    };

    return doctor;
};
