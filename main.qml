// Quick PyQt5 / QML popup message demo for BKG
// 2023-FEB-21 steve.richardson@makeitlabs.com

import QtQuick 2.5
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.2

ApplicationWindow {
    width: 1000
    height: 200
    x: 0
    y: 0
    title: "HelloApp"

    flags: Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint

    property bool isVisible: false;
    property var message: "";

    visible: isVisible

    Connections {
        target: worker

        function onTextReady(text) {
            message = text;
            isVisible = true;
            showTimer.start();
        }
    }

    function setText(text) {
        message = text;
    }

    Timer {
        id: showTimer
        interval: 2000
        running: false
        repeat: false
        onTriggered: {
            isVisible = false;
        }
    }

    Text {
        anchors.centerIn: parent
        text: message
        font.pixelSize: 24
    }

}