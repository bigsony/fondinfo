/*
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - tomamic@ce.unipr.it - 2010
 *
 * This is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include "loader.h"
#include "game.h"
#include "ball.h"
#include "paddle.h"
#include "autopaddle.h"

#include <fstream>
#include <sstream>
#include <QtCore/QFile>
#include <QtCore/QTextStream>

using namespace std;

Loader::Loader(string name)
{
    this->name = name;
}

Game* Loader::loadGame(int level)
{
    QFile file(QString("%1-%2.dat").arg(name.c_str()).arg(level));
    file.open(QIODevice::ReadOnly | QIODevice::Text);
    istringstream in(QTextStream(&file).readAll().toStdString());

    int h, w, y, x;
    char type;

    in >> h >> w;
    Game* game = new Game(h, w);

    in >> type >> y >> x;
    while (in.good()) {
        if (type == Ball::SYMBOL) {
            new Ball(game, y, x);
        } else if ('0' <= type && type <= '9') {
            new Paddle(game, y, x, type - '0');
        } else if ('A' <= type && type <= 'Z') {
            new AutoPaddle(game, y, x, type);
        }
        in >> type >> y >> x;
    }
    return game;
}
